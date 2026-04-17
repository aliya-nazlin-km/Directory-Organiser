# File Organizer (v1) — Documentation

## Table of Contents

1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [How It Works](#how-it-works)
4. [Code Structure](#code-structure)

   * [DIRECTORIES](#directories)
   * [get_directory()](#get_directorysuffix)
   * [organise_directory()](#organise_directorybase_path)
5. [Design Principles (SOLID)](#design-principles-solid)
6. [Key Design Decisions](#key-design-decisions)
7. [Limitations (v1)](#limitations-v1)
8. [Future Enhancements](#future-enhancements)
9. [Conclusion](#conclusion)

---

## Overview

The File Organizer is a Python-based utility script that organizes files in a user-specified directory into categorized folders based on their file extensions.

The goal of this project is to automate manual file sorting and demonstrate clean, maintainable code design.

---

## Problem Statement

Directories such as Downloads often become cluttered with various file types. Manually organizing these files is repetitive and inefficient.

This script addresses the problem by automatically:

* Identifying file types
* Categorizing files
* Moving them into appropriate directories

---

## How It Works

1. Accepts a directory path from the user
2. Iterates through all items in the directory
3. Skips subdirectories
4. Extracts file extension
5. Matches extension with predefined categories
6. Creates category folders if they do not exist
7. Moves files into their respective folders

---

## Code Structure

### DIRECTORIES

A dictionary mapping folder names to lists of file extensions.

---

### get_directory(suffix)

Determines the appropriate directory for a given file extension.

---

### organise_directory(base_path)

Main function responsible for:

* Validating input path
* Iterating through files
* Creating directories
* Moving files

---

## Design Principles (SOLID)

### Single Responsibility Principle (SRP)

Each function has a single responsibility:

* get_directory(): Determines file category
* organise_directory(): Handles file organization

---

### Open/Closed Principle (OCP)

New file types can be supported by updating the DIRECTORIES dictionary without changing existing logic.

---

### Liskov Substitution Principle (LSP)

Functions behave consistently for all valid inputs.

---

### Interface Segregation Principle (ISP)

Functions only depend on the inputs they require.

---

### Dependency Inversion Principle (DIP)

The script uses pathlib, avoiding platform-specific implementations.

---

## Key Design Decisions

* Used pathlib for cleaner file handling
* Used dictionary-based categorization
* Ignored subdirectories for simplicity
* Used extension-based classification

---

## Limitations (v1)

* Does not handle duplicate filenames
* Does not process subdirectories
* Categorization is based only on file extensions
* No logging or detailed error handling

---

## Future Enhancements

* Duplicate file handling
* Recursive directory traversal
* CLI argument support
* GUI-based interface

---

## Conclusion

This project demonstrates a clean and modular approach to solving file organization with a focus on simplicity and maintainability.
