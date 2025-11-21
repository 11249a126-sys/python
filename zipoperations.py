import os
import zipfile

def backup_folder_to_zip(folder_name):
    # Ensure the folder exists
    if not os.path.exists(folder_name):
        print(f"Folder '{folder_name}' does not exist!")
        return

    # Name of the zip file
    zip_filename = f"{folder_name}_backup.zip"

    # Create a ZipFile object in write mode
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the folder and add files to the zip
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                # Write the file into zip, preserving the folder structure
                arcname = os.path.relpath(file_path, folder_name)
                zipf.write(file_path, arcname)

    print(f"Folder '{folder_name}' has been backed up to '{zip_filename}'")

# Example usage
folder_to_backup = "my_folder"  # Replace with your folder name
backup_folder_to_zip(folder_to_backup)
