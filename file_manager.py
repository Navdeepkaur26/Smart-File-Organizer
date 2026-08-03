import os
import shutil

from utils import create_folder, get_unique_filename, write_log


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".txt", ".csv"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".c", ".java", ".html", ".css", ".js"],
}


def organize_files(folder_path):

    summary = {
        "Images": 0,
        "Videos": 0,
        "Audio": 0,
        "Documents": 0,
        "Archives": 0,
        "Code": 0,
        "Others": 0
    }

    files = os.listdir(folder_path)

    for file in files:

        full_path = os.path.join(folder_path, file)

        if not os.path.isfile(full_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        folder_name = "Others"

        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                folder_name = category
                break

        destination = os.path.join(folder_path, folder_name)

        create_folder(destination)

        new_name = get_unique_filename(destination, file)

        shutil.move(
            full_path,
            os.path.join(destination, new_name)
        )

        write_log(new_name, folder_name)

        summary[folder_name] += 1

    return summary