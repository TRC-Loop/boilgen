#!/usr/bin/env python3

import os
import sys
import timeit

TEMPLATES = {
    "python": {
        "flask": {
            "templates/": "dir",
            "static/": "dir",
            "app.py": "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef index():\n\treturn 'Hello World!'\nif __name__ == '__main__':\n\tapp.run(debug=True)"
        },
        "basic": {
            "main.py": "if __name__ == '__main__':\n\tprint('Hello World!')"
        },
        "django": {
            "project/": "dir",
            "manage.py": "import django\nfrom django.core.management import execute_from_command_line\nimport sys\n\nif __name__ == '__main__':\n\texecute_from_command_line(sys.argv)"
        },
        "typer": {
            "main.py": "import typer\napp = typer.Typer()\n@app.command()\ndef hello(name: str):\n\tprint(f'Hello {name}!')\nif __name__ == '__main__':\n\tapp()"
        },
        "pygame": {
            "assets/": "dir",
            "assets/images/": "dir",
            "assets/music/": "dir",
            "assets/sounds/": "dir",
            "menus/": "dir",
            "main.py": "import pygame\nimport sys\nfrom menus import main_menu\n\n# Initialize Pygame\npygame.init()\n\n# Setup\nscreen = pygame.display.set_mode((800, 600))\npygame.display.set_caption('Pygame Template')\nclock = pygame.time.Clock()\n\n# Main Game Loop\ndef game_loop():\n\trunning = True\n\twhile running:\n\t\tfor event in pygame.event.get():\n\t\t\tif event.type == pygame.QUIT:\n\t\t\t\trunning = False\n\n\t\t# Game Logic Here\n\t\tscreen.fill((0, 0, 0))\n\n\t\tpygame.display.flip()  # Update the screen\n\n\t\tclock.tick(60)  # 60 frames per second\n\n\tpygame.quit()\n\tsys.exit()\n\nif __name__ == '__main__':\n\tmain_menu()\n\tgame_loop()",
            "menus/main_menu.py": "import pygame\n\n# Setup Menu Screen\ndef main_menu():\n\t# Display background\n\tscreen = pygame.display.get_surface()\n\tbg_color = (255, 255, 255)\n\tscreen.fill(bg_color)\n\n\t# Menu text\n\tfont = pygame.font.SysFont('Arial', 48)\n\ttext = font.render('Main Menu', True, (0, 0, 0))\n\tscreen.blit(text, (250, 100))\n\n\t# Start Button\n\tstart_button = pygame.Rect(300, 250, 200, 50)\n\tpygame.draw.rect(screen, (0, 255, 0), start_button)\n\tstart_text = font.render('Start Game', True, (255, 255, 255))\n\tscreen.blit(start_text, (350, 260))\n\n\t# Check if Start Button is clicked\n\tpygame.display.flip()\n\n\twhile True:\n\t\tfor event in pygame.event.get():\n\t\t\tif event.type == pygame.QUIT:\n\t\t\t\tpygame.quit()\n\t\t\t\tquit()\n\t\t\tif event.type == pygame.MOUSEBUTTONDOWN:\n\t\t\t\tif start_button.collidepoint(event.pos):\n\t\t\t\t\treturn"
        },
        "ursina": {
            "assets/": "dir",
            "assets/textures/": "dir",
            "assets/models/": "dir",
            "main.py": "from ursina import *\n\napp = Ursina()\n\n# Create a simple 3D cube\ncube = Entity(model='cube', color=color.red, scale=(2,2,2))\n\n# Simple movement with WASD keys\ndef update():\n\tif held_keys['w']:\n\t\tcube.y += 1 * time.dt\n\tif held_keys['s']:\n\t\tcube.y -= 1 * time.dt\n\tif held_keys['a']:\n\t\tcube.x -= 1 * time.dt\n\tif held_keys['d']:\n\t\tcube.x += 1 * time.dt\n\napp.run()"
        },
        "flask_restful": {
            "app.py": "from flask import Flask\nfrom flask_restful import Api, Resource\n\napp = Flask(__name__)\napi = Api(app)\n\nclass HelloWorld(Resource):\n\tdef get(self):\n\t\treturn {'message': 'Hello World!'}\n\napi.add_resource(HelloWorld, '/')\n\nif __name__ == '__main__':\n\tapp.run(debug=True)"
        }
    },
    "c": {
        "basic": {
            "main.c": "#include <stdio.h>\nint main() {\n\tprintf(\"Hello World!\\n\");\n\treturn 0;\n}"
        },
        "flag": {
            "main.c": "#include <stdio.h>\n#include <stdlib.h>\n#include <getopt.h>\n\nint main(int argc, char *argv[]) {\n\tint option;\n\twhile ((option = getopt(argc, argv, \"f:v\")) != -1) {\n\t\tswitch (option) {\n\t\t\tcase 'f':\n\t\t\t\tprintf(\"Flag -f with value: %s\\n\", optarg);\n\t\t\t\tbreak;\n\t\t\tcase 'v':\n\t\t\t\tprintf(\"Flag -v\\n\");\n\t\t\t\tbreak;\n\t\t\tdefault:\n\t\t\t\tprintf(\"Usage: %s [-f value] [-v]\\n\", argv[0]);\n\t\t\t\treturn 1;\n\t\t}\n\t}\n\treturn 0;\n}"
        }
    },
    "go": {
        "basic": {
            "main.go": "package main\nimport \"fmt\"\nfunc main() {\n\tfmt.Println(\"Hello World!\")\n}"
        },
        "flag": {
            "main.go": "package main\nimport (\n\t\"flag\"\n\t\"fmt\"\n)\n\nfunc main() {\n\tvar name string\n\tvar age int\n\tflag.StringVar(&name, \"name\", \"John\", \"Enter your name\")\n\tflag.IntVar(&age, \"age\", 30, \"Enter your age\")\n\tflag.Parse()\n\n\tfmt.Printf(\"Hello %s, you are %d years old.\", name, age)\n}"
        }
    },
    "javascript": {
        "node": {
            "server.js": "const http = require('http');\nconst server = http.createServer((req, res) => {\n\tres.writeHead(200, {'Content-Type': 'text/plain'});\n\tres.end('Hello World!');\n});\nserver.listen(3000, () => console.log('Server running on port 3000'));"
        },
        "react": {
            "src/": "dir",
            "public/": "dir",
            "package.json": "{\n\t\"name\": \"react-app\",\n\t\"version\": \"1.0.0\",\n\t\"dependencies\": {\n\t\t\"react\": \"^18.0.0\",\n\t\t\"react-dom\": \"^18.0.0\"\n\t}\n}"
        }
    },
    "website": {
        "html_css_js": {
            "index.html": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>Hello World</title>\n\t<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n\t<h1>Hello World!</h1>\n\t<script src='script.js'></script>\n</body>\n</html>",
            "style.css": "body { font-family: Arial, sans-serif; text-align: center; }",
            "script.js": "document.addEventListener('DOMContentLoaded', () => console.log('Hello World!'));"
        }
    },
    "java": {
        "basic": {
            "Main.java": "public class Main {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println(\"Hello World!\");\n\t}\n}"
        }
    },
    "kotlin": {
        "basic": {
            "Main.kt": "fun main() {\n\tprintln(\"Hello World!\")\n}"
        }
    },
    "csharp": {
        "console": {
            "Program.cs": "using System;\nclass Program {\n\tstatic void Main() {\n\t\tConsole.WriteLine(\"Hello World!\");\n\t}\n}"
        },
        "aspnet": {
            "Controllers/": "dir",
            "Views/": "dir",
            "Program.cs": "using Microsoft.AspNetCore.Builder;\nusing Microsoft.AspNetCore.Hosting;\nusing Microsoft.Extensions.Hosting;\n\nvar builder = WebApplication.CreateBuilder(args);\nvar app = builder.Build();\napp.MapGet(\"/\", () => \"Hello World!\");\napp.Run();"
        }
    }
}


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def usage():
    print(bcolors.HEADER + bcolors.UNDERLINE + "USAGE" + bcolors.ENDC)
    print(f"{bcolors.BOLD}boilgen{bcolors.ENDC} <Language> <Type>")
    print(bcolors.HEADER + bcolors.UNDERLINE + "AVAILABLE TEMPLATES" + bcolors.ENDC)
    templates_lang = TEMPLATES.keys()
    for lang_template in templates_lang:
        print(bcolors.OKCYAN + "[" + bcolors.ENDC + bcolors.BOLD + lang_template.title() + bcolors.ENDC + bcolors.OKCYAN + "]" + bcolors.ENDC)
        templates_p_lang = TEMPLATES[lang_template].keys()
        for p_template in templates_p_lang:
            print(" " + p_template)

if __name__ == "__main__":
    args = sys.argv
    if not len(args) == 3:
        usage()
        sys.exit(1)
    
    lang_template = args[1].lower()
    type_template = args[2].lower()
    
    if not lang_template in TEMPLATES:
        print("Template: " + lang_template + " not found. Type 'boilgen help' for all templates")
        sys.exit(1)
    
    if not type_template in TEMPLATES[lang_template]:
        print("Template type: " + type_template + " not found in: " + lang_template + ". Type 'boilgen help' for all templates")
    
    print("Generating Boilerplate...")
    print("Path: " + str(os.getcwd()))
    start = timeit.default_timer()
    
    template = TEMPLATES[lang_template][type_template]
    
    files, dirs = 0, 0
    
    for action in template:
        if template[action] == "dir":
            if os.path.exists(action):
                print(f"{bcolors.FAIL}[-]{bcolors.ENDC} Directory already exists: {bcolors.OKCYAN}{action}{bcolors.ENDC} Skipping...")
                continue
            print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} Creating directory: {bcolors.OKCYAN}" + action + bcolors.ENDC)
            os.makedirs(action)
            dirs += 1
        else:
            if os.path.exists(action):
                print(f"{bcolors.FAIL}[-]{bcolors.ENDC} File already exists: {bcolors.OKCYAN}{action}{bcolors.ENDC} Skipping...")
                continue
            print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} Creating file: {bcolors.OKCYAN}" + action + bcolors.ENDC)
            with open(action, "w") as f:
                f.write(template[action])
            files += 1
    stop = timeit.default_timer()
    total_time = stop - start

    mins, secs = divmod(total_time, 60)

    print(f"{bcolors.OKGREEN}{bcolors.BOLD}Finished!{bcolors.ENDC} Took: {bcolors.OKCYAN}{round(secs, 4)}{bcolors.ENDC}s, created {bcolors.OKCYAN}{dirs}{bcolors.ENDC} {"Directory" if dirs == 1 else "Directories"}, {bcolors.OKCYAN}{files}{bcolors.ENDC} {"File" if files == 1 else "Files"} (Total: {bcolors.OKCYAN}{files+dirs}{bcolors.ENDC})")