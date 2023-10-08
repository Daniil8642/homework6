import shutil
import sys
import scan
import normalize
from pathlib import Path
import files_generator
from files_generator import file_generator
import os


def move_image_file(file, root_folder):
    image_folder = root_folder / "images"
    image_folder.mkdir(exist_ok=True)
    new_name = normalize.normalize(file.name)
    new_path = image_folder / new_name
    file.rename(new_path)

def move_document_file(file, root_folder):
    document_folder = root_folder / "documents"
    document_folder.mkdir(exist_ok=True)
    new_name = normalize.normalize(file.name)
    new_path = document_folder / new_name
    file.rename(new_path)

def move_audio_file(file, root_folder):
    audio_folder = root_folder / "audio"
    audio_folder.mkdir(exist_ok=True)
    new_name = normalize.normalize(file.name)
    new_path = audio_folder / new_name
    file.rename(new_path)

def move_video_file(file, root_folder):
    video_folder = root_folder / "video"
    video_folder.mkdir(exist_ok=True)
    new_name = normalize.normalize(file.name)
    new_path = video_folder / new_name
    file.rename(new_path)



def main(folder_path):
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        move_image_file(file, folder_path)

    for file in scan.jpg_files:
        move_image_file(file, folder_path)

    for file in scan.png_files:
        move_image_file(file, folder_path)

    for file in scan.txt_files:
        move_document_file(file, folder_path)

    for file in scan.docx_files:
        move_document_file(file, folder_path)

    for file in scan.audio_files:
        move_audio_file(file, folder_path)

    for file in scan.video_files:
        move_video_file(file, folder_path)


def remove_empty_folders(root_folder):
    for folder in root_folder.iterdir():
        if folder.is_dir():
            try:
                folder.rmdir()
                print(f"Удалена пустая папка: {folder}")
            except OSError as e:
                print(f"Ошибка при удалении пустой папки: {folder}, {e}")


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    files_generator.file_generator(arg)
    main(arg.resolve())

    remove_empty_folders(arg.resolve())