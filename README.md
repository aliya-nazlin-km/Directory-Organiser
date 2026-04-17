# 📂 File Organizer (v1)

A simple Python script to automatically organize files in a directory into categorized folders based on their file extensions.

---

## 🚀 Features

* Organizes files into categories:

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
* Automatically creates folders if they do not exist
* Moves files into their respective directories
* Simple and beginner-friendly implementation

---

## 🛠️ Tech Stack

* Python 3
* pathlib (standard library)

---

## 📁 Folder Structure (After Running)

Example:

Before:

```bash
Downloads/
    file.pdf
    image.jpg
    song.mp3
```

After:

```bash
Downloads/
    DOCUMENTS/
        file.pdf
    IMAGES/
        image.jpg
    AUDIOS/
        song.mp3
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/aliya-nazlin-km/file-organizer.git
```

2. Navigate to the project folder:

```bash
cd file-organizer
```

3. Run the script:

```bash
python organizer.py
```

4. Enter the directory path when prompted:

```bash
Enter the directory path to organize: D:\Downloads
```

---

## 📌 How It Works

1. Takes a directory path as input
2. Iterates through all files in the directory
3. Identifies file type using extension
4. Matches it with predefined categories
5. Creates category folders if needed
6. Moves files into respective folders

---

## ⚠️ Limitations (v1)

* Does not handle duplicate filenames (may overwrite or fail)
* Does not process subdirectories
* Only works on top-level files
* Categorization is based only on file extensions

---

## 🔮 Future Improvements

* Duplicate file handling
* Recursive directory support
* CLI arguments support
* Logging and reporting
* GUI version

---

## 👩‍💻 Author

**Aliya Nazlin KM**
GitHub: https://github.com/aliya-nazlin-km

---

## 📜 License

This project is open-source and available under the MIT License.
