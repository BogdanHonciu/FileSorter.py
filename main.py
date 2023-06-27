import os
import shutil

# specify the directory you want to sort
source_directory = r"C:/Users/honci/OneDrive/Desktop\PROJECTS/File sorter/files for sorting/"

try:
    # get a list of all files in the source directory
    file_list = os.listdir(source_directory)

    # create a folder for each file extension
    for file_name in file_list:
        file_extension = os.path.splitext(file_name)[1][1:]
        destination_folder = os.path.join(source_directory, file_extension)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # move the file to the appropriate folder
        source_path = os.path.join(source_directory, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
except Exception as e:
    print(f"An error occurred while sorting the files: {e}")