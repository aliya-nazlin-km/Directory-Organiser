from pathlib import Path

DIRECTORIES = {
    "DOCUMENTS": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],

    "SPREADSHEETS": [".xls", ".xlsx", ".csv", ".ods"],

    "PRESENTATIONS": [".ppt", ".pptx", ".pps", ".odp"],

    "IMAGES": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],

    "AUDIOS": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".m4b"],

    "VIDEOS": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],

    "ARCHIVES": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],

    "EXECUTABLES": [".exe", ".msi", ".bat", ".cmd", ".sh", ".apk", ".deb", ".rpm"],

    "CODE": [".py", ".java", ".c", ".cpp", ".h", ".hpp", ".js", ".ts",
             ".html", ".css", ".sql", ".json", ".xml", ".yaml", ".yml"],

    "FONTS": [".ttf", ".otf", ".woff", ".woff2"]
}


'''
This code takes the file type (suffix) as input and compares that suffix with the suffixes in each 
directory category from DIRECTORIES dictionary. If suffix doesn't match any category, returns MISC
as directory name
'''
def get_directory(suffix):
    for directory_name, suffixes in DIRECTORIES.items():
        if suffix in suffixes:
            return directory_name
    return "MISC"


'''
This function ensures that duplicate file names are handled safely.
If a file with the same name already exists in the destination directory,
it appends a counter like (1), (2), etc. to create a unique filename.
'''
def get_unique_name(path):
    counter = 1
    new_path = path

    # Keep checking until a non-existing filename is found
    while new_path.exists():
        new_name = f"{path.stem} ({counter}){path.suffix}" #stem is file name without extension
        new_path = path.with_name(new_name)
        counter += 1

    return new_path


'''
This code fetches and organises the files in the directory chosen by the user
'''
def organise_directory(base_path):
    # Path entered by user is fetched
    base_path = Path(base_path)

    # Checks if the path is correct/exists
    if not base_path.exists():
        print("Invalid path!")
        return

    # Checks if the path is that of a directory, if not, terminate the program
    if not base_path.is_dir():
        print("Invalid! Please enter a DIRECTORY path")
        return

    else:  # If path is that of a directory
        for item in base_path.iterdir():  # Fetch each item from the directory by iterating through
            if item.is_dir():  # If the item is a subdirectory, skip and continue without any action
                continue

            filetype = item.suffix.lower()
            directory = get_directory(filetype)  # Use the file type and fetch the directory to which it should belong
            directory_path = base_path / directory  # Push the directory into base directory

            if not directory_path.exists():  # If the directory does not exist,
                directory_path.mkdir()  # Create the directory

            # Handle duplicate filenames safely
            destination = directory_path / item.name
            destination = get_unique_name(destination)

            # Move file to the appropriate directory
            item.rename(destination)

        print("Directory Organised Successfully!")


# Take input from user
user_path = input("Enter the directory path to organize: ")
organise_directory(user_path)
