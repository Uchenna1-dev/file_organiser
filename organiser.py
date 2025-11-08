import os #for file and directory operations
import shutil  #for moving files

# 1. Define the folder you want to organize
source_folder = "/workspaces/file_organiser/test_folder"

# 2. Define the file categories
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}

# 3. Loop through all files in the source folder that contains files to be organised
for filename in os.listdir(source_folder):
            
            #First create a path for the filenames as you would need it later to check if items in source_folder (filename)\
            #are files not folders
            source_path = os.path.join(source_folder, filename)
            #check if item is file not a subfolder
            if os.path.isfile(source_path):
                            #get each of their file types, e.g. document.pdf which is a pdf.
                            name, filetype = os.path.splitext(filename) #this gives you the name and the file type with the '.'

                            #check to see if filetype is in file_types dictionary, if so, create and store it in its category
                            for category, extension in file_types.items():
                    
                                    if filetype in extension:
                                            #first you have to define the destination_folder, which is where you are storing the file
                                            destination_folder = os.path.join(source_folder, category)
                                            #This creates the desitnation folder called the category name in the source folder. If folder already exists then it moves on without producing error messages.
                                            os.makedirs(destination_folder, exist_ok = True)
                                            #This actually moves the file from its source to its destination. The 'Path' is needed.
                                            destination_path = os.path.join(destination_folder,filename)
                                            shutil.move(source_path, destination_path)
                                            break


            else:
                    continue # this skips over the folders.
            
                
                                           
                                

