import os
import shutil

def create_folder(folder_name, path):
    """Create a folder if it doesn't already exist."""
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def organize_files(directory):
    """Organize files in the given directory based on their extensions."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension:
            folder_name = file_extension[1:]  # Remove the dot from the extension
        else:
            folder_name = "no_extension"

        # Create a folder for the file extension and move the file
        folder_path = create_folder(folder_name, directory)
        shutil.move(file_path, os.path.join(folder_path, file_name))

    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    # Input the directory to organize
    folder_to_organize = input("Enter the path of the folder to organize: ").strip()
    organize_files(folder_to_organize)
