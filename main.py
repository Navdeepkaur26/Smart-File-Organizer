import os
import shutil
from tkinter import Tk, filedialog

# Hide tkinter window
root = Tk()
root.withdraw()

# Select folder
folder_path = filedialog.askdirectory(title="Select Folder")

if folder_path:

    files = os.listdir(folder_path)

    for file in files:

        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):

            file_name, extension = os.path.splitext(file)
            extension = extension.lower()

            # Images
            if extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:

                destination = os.path.join(folder_path, "Images")

            # PDFs
            elif extension == ".pdf":

                destination = os.path.join(folder_path, "PDFs")

            # Videos
            elif extension in [".mp4", ".mkv", ".avi", ".mov"]:

                destination = os.path.join(folder_path, "Videos")

            # Audio
            elif extension in [".mp3", ".wav"]:

                destination = os.path.join(folder_path, "Audio")

            # Documents
            elif extension in [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"]:

                destination = os.path.join(folder_path, "Documents")

            # Others
            else:

                destination = os.path.join(folder_path, "Others")

            # Create folder if not exists
            if not os.path.exists(destination):
                os.mkdir(destination)

            # Move file
            shutil.move(full_path, os.path.join(destination, file))

            print(f"Moved : {file}")

    print("\n✅ All files organized successfully!")

else:
    print("No folder selected.")