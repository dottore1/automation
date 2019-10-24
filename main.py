import os
from pathlib import Path

DIRECTORIES = {
    "DOCUMENTS": [".pdf", ".docx", ".xlsx", ".txt"],
    "PICTURES": [".jpg", ".png", ".gif", ".psd", ".PNG"],
    "INSTALLERS": [".exe"],
    "WEB": [".html",".xml", ".js"],
    "ZIPPERS": [".zip"]
}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


#This will organise your files


def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
    try:
        os.mkdir("OTHERS")
    except:
        pass
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER/' + str(Path(dir)))
        except:
            pass


if __name__ == "__main__":
    organize()