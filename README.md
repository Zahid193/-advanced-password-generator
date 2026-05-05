# 🔐 Advanced Password Generator (Python CLI Tool)

A secure, customizable, and production-style password generator built with Python.
This tool uses **cryptographically secure randomness** to generate strong and unpredictable passwords suitable for real-world applications.

---

## 🚀 Features

* Generate strong and secure passwords
* Customizable password length
* Toggle character types:

  * Uppercase letters (A–Z)
  * Lowercase letters (a–z)
  * Digits (0–9)
  * Symbols (!@#$%^&* etc.)
* Ensures at least one character from each selected category
* Password strength checker (Weak / Medium / Strong)
* Save generated passwords to a file
* Command-line interface (CLI using argparse)

---

## 🧠 Security Focus

This project uses Python’s **`secrets` module** instead of `random`, ensuring:

* Cryptographic-level security
* Unpredictable password generation
* Suitable for real-world usage

---

## 🛠️ Tech Stack

* Python 3
* `secrets` module
* `argparse`
* `string` module

---

## 📦 Installation

1. Clone the repository:

git clone https://github.com/Zahid193/advanced-password-generator.git
cd advanced-password-generator

2. Run the script:

python generator.py

---

## ⚙️ Usage

### Default Usage

python generator.py

### Custom Password

python generator.py --length 16 --upper --lower --digits --symbols

### Save Password to File

python generator.py --length 12 --digits --symbols --save passwords.txt

---

## 📸 Example Output

Generated Password: G#7kL!9pQ@2xZ1
Strength: Strong
Saved to passwords.txt

---

## 🔍 Password Strength Criteria

| Strength | Conditions                               |
| -------- | ---------------------------------------- |
| Weak     | Short length or limited character types  |
| Medium   | Moderate length with some variation      |
| Strong   | 12+ length with multiple character types |

---

## 📁 Project Structure

advanced-password-generator/
│
├── generator.py
├── README.md
└── .gitignore

---

## 🔮 Future Improvements

* GUI version (Tkinter)
* Clipboard copy feature
* Password entropy calculation
* Web version using Flask
* Password manager integration

---

## ⚠️ Disclaimer

This project is created for **educational purposes only**.
Do not use this tool for unauthorized access, hacking, or any illegal activities.
The author is not responsible for any misuse of this software.

---

## 👨‍💻 Author

**Zahid Qureshi**

GitHub: https://github.com/Zahid193

---

## ⭐ Support

If you found this project helpful:

* Star the repository
* Fork it
* Share it

---

## 📌 Project Status

Active
Open for improvements
