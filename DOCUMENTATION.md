# File Organizer (v2) — Documentation

## Table of Contents

1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [How It Works](#how-it-works)
4. [Code Structure](#code-structure)

   * [DIRECTORIES](#directories)
   * [get_directory()](#get_directorysuffix)
   * [get_unique_name()](#get_unique_namepath)
   * [organise_directory()](#organise_directorybase_path)
5. [Design Principles (SOLID)](#design-principles-solid)
6. [Key Design Decisions](#key-design-decisions)
7. [Improvements from v1](#improvements-from-v1)
8. [Limitations](#limitations)
9. [Future Enhancements](#future-enhancements)
10. [Conclusion](#conclusion)

---

## Overview

The File Organizer is a Python-based utility script that organizes files into categorized folders based on their file extensions. Version 2 improves reliability by introducing duplicate file handling.

---

## Problem Statement

Managing unorganized directories can be inefficient. Additionally, moving files into categorized folders may lead to filename conflicts when duplicates exist.

This version addresses both problems by organizing files and safely handling duplicates.

---

## How It Works

1. Accepts a directory path
2. Iterates through all files
3. Determines file category
4. Creates folders if needed
5. Checks for duplicate filenames
6. Generates unique filenames when required
7. Moves files safely

---

## Code Structure

### DIRECTORIES

Defines mapping between file extensions and folder categories.

---

### get_directory(suffix)

Returns the appropriate directory name based on file extension.

---

### get_unique_name(path)

Handles duplicate file names.

* Checks if a file already exists in destination
* Appends `(1), (2), ...` until a unique name is found
* Returns a safe file path

---

### organise_directory(base_path)

Main function responsible for:

* Path validation
* Iterating through files
* Creating directories
* Handling duplicates
* Moving files

---

## Design Principles (SOLID)

### Single Responsibility Principle (SRP)

* `get_directory()` → categorization
* `get_unique_name()` → duplicate handling
* `organise_directory()` → coordination

---

### Open/Closed Principle (OCP)

New file types can be added by updating the DIRECTORIES dictionary without modifying logic.

---

### Liskov Substitution Principle (LSP)

Functions behave consistently for valid inputs.

---

### Interface Segregation Principle (ISP)

Functions accept only necessary inputs.

---

### Dependency Inversion Principle (DIP)

Relies on pathlib abstraction instead of OS-specific file handling.

---

## Key Design Decisions

* Introduced a dedicated duplicate handling function
* Used iterative approach for generating unique filenames
* Maintained extension-based classification for simplicity
* Preserved modular function design

---

## Improvements from v1

* Added duplicate file handling
* Prevents overwriting and runtime errors
* Enables safe repeated execution

---

## Limitations

* Does not process subdirectories
* Classification is extension-based only
* No logging or error tracking

---

## Future Enhancements

* Recursive directory traversal
* CLI argument support
* GUI-based interface

---

## Conclusion

Version 2 enhances the reliability of the file organizer by introducing duplicate handling while maintaining simplicity, modularity, and clean design principles.
