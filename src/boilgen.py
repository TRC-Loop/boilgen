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
        }
    },
    "c": {
        "basic": {
            "main.c": "#include <stdio.h>\nint main() {\n    printf(\"Hello World!\\n\");\n    return 0;\n}"
        }
    },
    "cpp": {
        "basic": {
            "main.cpp": "#include <iostream>\nint main() {\n    std::cout << \"Hello World!\\n\";\n    return 0;\n}"
        }
    },
    "go": {
        "basic": {
            "main.go": "package main\nimport \"fmt\"\nfunc main() {\n    fmt.Println(\"Hello World!\")\n}"
        }
    },
    "javascript": {
        "node": {
            "server.js": "const http = require('http');\nconst server = http.createServer((req, res) => {\n\tres.writeHead(200, {'Content-Type': 'text/plain'});\n\tres.end('Hello World!');\n});\nserver.listen(3000, () => console.log('Server running on port 3000'));"
        },
        "react": {
            "src/": "dir",
            "public/": "dir",
            "package.json": "{\n  \"name\": \"react-app\",\n  \"version\": \"1.0.0\",\n  \"dependencies\": {\n    \"react\": \"^18.0.0\",\n    \"react-dom\": \"^18.0.0\"\n  }\n}" 
        }
    },
    "website": {
        "html_css_js": {
            "index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Hello World</title>\n    <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n    <h1>Hello World!</h1>\n    <script src='script.js'></script>\n</body>\n</html>",
            "style.css": "body { font-family: Arial, sans-serif; text-align: center; }",
            "script.js": "document.addEventListener('DOMContentLoaded', () => console.log('Hello World!'));"
        }
    },
    "java": {
        "basic": {
            "Main.java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World!\");\n    }\n}" 
        }
    },
    "kotlin": {
        "basic": {
            "Main.kt": "fun main() {\n    println(\"Hello World!\")\n}" 
        }
    },
    "csharp": {
        "console": {
            "Program.cs": "using System;\nclass Program {\n    static void Main() {\n        Console.WriteLine(\"Hello World!\");\n    }\n}"
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