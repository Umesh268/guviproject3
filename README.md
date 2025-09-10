# Python Syntax Checker Tool

A lightweight web application built with Flask that allows users to quickly check Python code for syntax errors without running the code. Users can paste Python code or upload `.py` files to validate them using Python’s built-in `ast` module.

---

## 🚀 Features
- ✅ Check Python code syntax from a text input.
- ✅ Upload `.py` files and validate their syntax.
- ✅ Display error messages with line and column details.
- ✅ Simple and intuitive web interface.
- ✅ Built with Python’s `ast` module and Flask.

---

## 📂 Project Structure

```
my-flask-app/
├── app.py                # Main Flask application
├── uploads/              # Folder to store uploaded Python files
├── templates/
│   └── index.html        # HTML interface
└── README.md             # Documentation
```

---

## ⚙ Setup Instructions (macOS)

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd my-flask-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```
   or using Flask CLI:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   ```

5. **Open the app in your browser:**
   ```
   http://127.0.0.1:5000/
   ```

---

## 📥 How to Use

1. **Check Syntax**
   - Paste Python code into the text area.
   - Click “Check Syntax” to see if the code has any errors.

2. **Upload File**
   - Choose a `.py` file from your device.
   - Click “Upload” to validate the file’s syntax.

3. The results will show success or detailed error messages.

---

## 📦 Dependencies

- Python 3.x
- Flask
- Werkzeug (for file uploads)

Install with:
```bash
pip install flask
```

---

## 📈 Future Enhancements

- Support for Python version selection.
- Integration with formatters like `black`.
- UI improvements with CSS frameworks.
- Authentication and user management.

---
