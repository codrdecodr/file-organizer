# File Organizer

A simple Python script that organizes files in a given folder by sorting them into category subfolders based on file extensions.


## Features

- Sorts files into predefined categories: Images, Documents, Archives, Videos, and Others.
- Skips hidden files (those starting with a dot).
- Supports a dry-run mode to preview changes without moving files.
- Uses the console output with colored messages for clear feedback.

## Requirements

- Python 3.x
- `rich` library (for colored console output)

Install `rich` via pip if you don’t have it:

```bash
pip install rich
