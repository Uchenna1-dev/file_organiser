import os      # for working with files and folders
import shutil  # for moving files

# 1. Folder to organise
source_folder = "/workspaces/file_organiser/test_folder"

# 2. File categories and their extensions
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}

# 3. Loop through everything in the folder
for filename in os.listdir(source_folder):

    # Get the full path to each item
    source_path = os.path.join(source_folder, filename)

    # Check if the item is a file (ignore subfolders)
    if os.path.isfile(source_path):

        # Split the file name and extension (e.g., "photo.jpg" -> ".jpg")
        name, filetype = os.path.splitext(filename)

        # Find which category this file type belongs to
        for category, extensions in file_types.items():
            if filetype in extensions:

                # Create the destination folder (if it doesn’t already exist)
                destination_folder = os.path.join(source_folder, category)
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file into its matching folder
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)

                # Stop checking once a match is found
                break

    else:
        continue  # skip folders and move to the next item
