import os      # For working with files and folders
import shutil  # For moving files

# 1. Define the folder to organise
source_folder = "/workspaces/file_organiser/test_folder"

# 2. Define file categories and their extensions
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}

# 3. Loop through every item in the source folder
for filename in os.listdir(source_folder):

    # Get the full path to the current item
    source_path = os.path.join(source_folder, filename)

    # Only process files (ignore any existing folders)
    if os.path.isfile(source_path):

        # Split the file name and extension (e.g. “photo.jpg” → “photo”, “.jpg”)
        name, filetype = os.path.splitext(filename)

        # Assume the file doesn’t match any category yet
        match = False

        # Check each category in the dictionary
        for category, extensions in file_types.items():

            # If the file’s extension matches this category
            if filetype in extensions:
                match = True

                # Create the destination folder if it doesn’t already exist
                destination_folder = os.path.join(source_folder, category)
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file into its category folder
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)

                # Stop checking once a match has been found
                break

        # If no match was found, move the file into an “other” folder
        if match == False:
            destination_folder = os.path.join(source_folder, "other")
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)

    else:
        # Skip any folders and continue with the next item
        continue
