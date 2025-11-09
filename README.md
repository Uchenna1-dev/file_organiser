## file_organiser

A simple Python automation script that sorts files into organised folders based on their file type (e.g. documents, images, videos, archives).
Perfect for cleaning up messy directories such as your Downloads folder.

## Features

Automatically detects file types and organises them into categorised folders.

Supports common file formats (documents, images, videos, archives).

Includes an “Other” folder for files that do not match any known category.

Easily customisable — add or remove categories and file extensions.

Prevents overwriting or deleting existing files.

## How It Works

Specify the folder path you want to organise inside the script.

The programme scans all files within that directory.

Each file is moved into a corresponding subfolder:

Documents → .pdf, .docx, .txt, .xlsx

Images → .jpg, .jpeg, .png

Videos → .mp4, .mov

Archives → .zip, .rar

Any files that do not fit these categories are moved to an “Other” folder.
This ensures every file has a place without being skipped or lost.

## Example Folder Structure

After running the script:

Downloads/
│
├── organiser.py
│
├── Documents/
│   ├── report.pdf
│   ├── notes.txt
│
├── Images/
│   ├── photo.jpg
│
├── Videos/
│   ├── clip.mp4
│
├── Archives/
│   ├── project.zip
│
└── Other/
    ├── randomfile.xyz

## Customisation

You can edit the file categories and extensions directly in the script by modifying the dictionary below:

file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}


Add or remove categories and file extensions as needed.

## Setup

Run the script using:

python organiser.py


Make sure to update the source_folder path at the top of the script to the directory you wish to organise.

## Requirements

Python 3.x

No additional modules are required beyond the built-in os and shutil libraries.

## Installation

Clone this repository and navigate into the folder:

git clone https://github.com/Uchenna1-dev/file_organiser.git
cd file_organiser

## Author

Created by Uchenna1-dev