# 🚀 Boilgen - The Ultimate Boilerplate Generator

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

### **Example Output**
```sh
Generating Boilerplate...
Path: /your/project/path
[+] Creating directory: templates/
[+] Creating directory: static/
[+] Creating file: app.py
Finished! Took: 0.0032s, created 2 Directories, 1 File (Total: 3)
```

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

---

## 📜 License
MIT License - Free to use and modify.

🚀 Happy Coding! 🎉

