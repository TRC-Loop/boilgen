# 🚀 Boilgen - The Ultimate Boilerplate Generator
<p align="center"><h2 align="center" style="margin:0;padding:0;">Create New Projects the fast way</h2><br><img src="https://github.com/TRC-Loop/boilgen/blob/main/static/boilgen.gif?raw=true" alt="Boilgen GIF"></p>


<p align="center">
  <img src="https://img.shields.io/github/v/release/TRC-Loop/Boilgen?label=Version&style=flat-square" alt="GitHub Release">
  <img src="https://img.shields.io/github/stars/TRC-Loop/boilgen?style=flat-square&label=Stars" alt="GitHub Repo stars">
  <img src="https://img.shields.io/github/languages/code-size/TRC-Loop/Boilgen?style=flat-square&label=Size%20(Code)" alt="GitHub code size">
  <img src="https://img.shields.io/github/license/TRC-Loop/boilgen?style=flat-square&label=License" alt="GitHub License">
</p>



Boilgen is a powerful and easy-to-use CLI tool that instantly generates project boilerplates for multiple languages and frameworks. Whether you're building a Flask app, a React project, or a simple C++ program, Boilgen has you covered!

## 🎯 Features
- ✅ Supports multiple languages: Python, C, C++, Go, JavaScript, Java, C#, and more!
- ✅ Instant setup with predefined templates
- ✅ Simple, fast, and lightweight
- ✅ Fully customizable

---

## 📥 Installation
### **1️⃣ Install via Script**
#### **Linux & macOS**
```sh
curl -sSL https://raw.githubusercontent.com/TRC-Loop/boilgen/main/install.sh | bash
```
#### **Windows (PowerShell)**
```powershell
iwr -useb https://raw.githubusercontent.com/TRC-Loop/boilgen/main/install.ps1 | iex
```

### **2️⃣ Manual Installation**
```sh
git clone https://github.com/TRC-Loop/boilgen.git ~/.boilgen
ln -s ~/.boilgen/src/boilgen.py ~/.local/bin/boilgen
chmod +x ~/.local/bin/boilgen
```

> **Note:** Ensure `~/.local/bin` is in your `PATH`.
> 
> **Updating** Re-Run the Installation Script. (The old Installation will be __deleted__ and boilgen will then be installed)
---

## 🚀 Usage
Once installed, you can run `boilgen` from anywhere in your terminal.

### **Show Available Templates**
```sh
boilgen help
```

### **Generate a Project**
```sh
boilgen <language> <type>
```
Example:
```sh
boilgen python flask
```
This creates a Flask project structure in your current directory! 🎉

---

## 🔥 Supported Languages & Frameworks
| Language    | Type |
|------------|------|
| Python     | Flask, Django, Typer, Basic |
| JavaScript | Node, React |
| C          | Basic |
| C++        | Basic |
| Go         | Basic |
| Java       | Basic |
| C#         | Console, ASP.NET |
| Website    | HTML+CSS+JS |

---

## 🛠 Uninstall
If you ever need to remove Boilgen, simply run:
```sh
rm -rf ~/.boilgen ~/.local/bin/boilgen
```

---

## 💡 Contributing
Want to add more templates or improve the script? Feel free to fork the repo and submit a pull request!

### The Template format
```python
"python": {
  "flask": {
      "templates/": "dir",
      "static/": "dir",
      "app.py": "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef index():\n\treturn 'Hello World!'\nif __name__ == '__main__':\n\tapp.run(debug=True)"
  },
```
Use the Key as the file/folder name.

Use `dir` (lowercase) as a value for folders, else, a file with that content will be created.

Use `\n`for New Lines in code and `\t` for Tabs.

> **Note**: Template (Language and Type) Names should _always_ be lowercase. Else it might not work!

---

## 📜 License
MIT License - Free to use and modify.

