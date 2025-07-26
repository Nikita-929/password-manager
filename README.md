# password-manager
# 🔐 Password Manager

A simple and secure Password Manager built using Python and Tkinter. It allows you to:

- Generate strong, random passwords
- Save login credentials securely to a local JSON file
- Search and retrieve credentials quickly
- Auto-copy passwords to your clipboard

---

## 📂 Features

- ✅ Generate secure passwords with letters, numbers, and symbols  
- ✅ Save website, email, and password to a JSON file  
- ✅ Search for saved credentials  
- ✅ Auto-copy generated password to clipboard  
- ✅ Basic error handling for empty fields and missing data  

---

## 🛠️ Tech Stack

- Python 3.x  
- Tkinter (for GUI)  
- JSON (for local data storage)  
- `pyperclip` (to copy password to clipboard)  

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed.  
Download: https://www.python.org/downloads/

Install the required package:

```bash
pip install pyperclip
```

---

## 📦 How to Run

1. Clone the repository or download the project files.
2. Ensure you have a `logo.png` image in the same folder (200x200 pixels recommended).
3. Run the application:

```bash
python main.py
```

> Replace `main.py` with your actual filename if different.

---

## 🧪 Example JSON Data Format

The saved credentials are stored in `data.json` in the following format:

```json
{
  "example.com": {
    "email": "user@example.com",
    "password": "securepassword123!"
  }
}
```

---

## 📌 Usage Tips

- Click **"Generate Password"** to create a random secure password and auto-copy it.
- Use the **"Add"** button to save the credentials.
- Use the **"Search"** button to retrieve saved credentials for a specific website.

---

## 🛡️ Disclaimer

This is a beginner-level project intended for learning purposes.  
For real-world password management, use secure, encrypted tools like Bitwarden or 1Password.

---

