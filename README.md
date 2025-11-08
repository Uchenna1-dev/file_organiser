## file_organiser
A simple Python automation script that sorts files into organised folders based on their file type (e.g., documents, images, videos, archives).
Perfect for cleaning up messy directories such as your Downloads folder.

## Features
Automatically detects file types and organises them into categorised folders.
Supports common file formats (documents, images, videos, archives).
Easily customisable — add new categories and extensions.
Prevents overwriting existing files.

## How It Works
Specify the folder path you want to organise in the script.
The programme scans all files in that directory.
Each file is moved into a corresponding subfolder (e.g., Documents, Images, Videos, Archives).
Archive files (e.g., .zip, .rar) are moved to the Archives folder.

## Setup
Run the script using:

python organiser.py

## Example folder structure after running
Downloads/
│
├── organiser.py
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
└── Archives/
    ├── project.zip

## Customisation

Edit the file_types dictionary in the script to adjust which extensions belong to each 
category:

file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}

## Requirements
Python 3.x

## Installation
Clone this repository and navigate into the folder:

git clone https://github.com/Uchenna1-dev/file_organiser.git

cd file_organiser

## Author
Created by Uchenna1-dev.