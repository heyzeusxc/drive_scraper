import os

files = []


def find_files(folder):
    try:
        for x in os.scandir(folder):
            if x.is_file():
                files.append([x.path, os.path.getsize(x.path)])
            elif x.is_dir():
                find_files(x.path)
            elif "drive_scraper" in x.path:
                pass
    except WindowsError:
        pass
    return files
