import os
from datetime import datetime


def create_folder(path):

    if not os.path.exists(path):
        os.makedirs(path)


def get_unique_filename(destination, filename):

    name, extension = os.path.splitext(filename)

    counter = 1

    new_filename = filename

    while os.path.exists(os.path.join(destination, new_filename)):

        new_filename = f"{name} ({counter}){extension}"
        counter += 1

    return new_filename


def write_log(file_name, folder_name):

    with open("organizer_log.txt", "a", encoding="utf-8") as file:

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        file.write(
            f"{current_time} -> {file_name} moved to {folder_name}\n"
        )