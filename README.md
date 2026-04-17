# 📂 File Organizer (v2)

A Python utility script to organize files in a directory into categorized folders based on file extensions. Version 2 introduces safe duplicate file handling to prevent overwriting.

---

## 🚀 Features

* 📁 Organizes files into categories:

  * Documents
  * Images
  * Videos
  * Audios
  * Code files
  * Archives
  * Executables
  * Fonts
  * Spreadsheets
  * Presentations
* 📦 Automatically creates folders if they do not exist
* 🔄 Moves files into their respective directories
* 🛡️ Handles duplicate filenames safely (e.g., `file (1).txt`)
* ✨ Simple and maintainable implementation

---

## 🛠️ Tech Stack

* Python 3
* pathlib (standard library)

---

## 📸 Example

### Before

```bash
Downloads/
    file.txt
    file.txt
    image.jpg
```

### After

```bash
Downloads/
    DOCUMENTS/
        file.txt
        file (1).txt
    IMAGES/
        image.jpg
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/aliya-nazlin-km/file-organizer.git
```

2. Navigate to the project directory:

```bash
cd file-organizer
```

3. Run the script:

```bash
python organizer.py
```

4. Enter the directory path:

```bash
Enter the directory path to organize: D:\Downloads
```

---

## ⚙️ How It Works

1. Accepts a directory path
2. Iterates through files
3. Identifies file type using extension
4. Maps file to a category
5. Creates folders if required
6. Checks for duplicate filenames
7. Renames duplicates safely
8. Moves files into respective folders

---

## ⚠️ Limitations

* Does not process subdirectories
* No logging or reporting

---

## 🔮 Future Enhancements

* 🔁 Recursive directory traversal
* 🖥️ CLI argument support
* 🪟 GUI-based interface

---

## 👩‍💻 Author

**Aliya Nazlin KM**
🔗 https://github.com/aliya-nazlin-km

---

## 📜 License

This project is licensed under the MIT License.
