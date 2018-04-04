import time
import os
import glob
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent
import shutil
import zipfile

DIR_TO_WATCH = "C:/Users/Sango/PycharmProjects/AWSLambdaSample"
DIR_TO_PUBLISH = "D:\AWSZips"
BASE_ZIP_NAME = "NicoNicoApiTest"
DIR_TO_ARCHIVE = "C:/Users/Sango/PycharmProjects/AWSLambdaSample"


def _zip_specified_directory():
    zipped_file = zipfile.ZipFile(
        os.path.join(DIR_TO_PUBLISH, BASE_ZIP_NAME + str(int(time.time())) + ".zip"),
        "w",
        zipfile.ZIP_DEFLATED)
    path = Path(DIR_TO_ARCHIVE)
    i = 0
    for item_name in map(lambda x: str(x), list(path.glob("**/*"))):
        i += 1
        if i <= 100:
            print(item_name)

        if ("venv" not in str(item_name)):
            zipped_file.write(item_name, os.path.relpath(item_name, DIR_TO_ARCHIVE))
    zipped_file.close()


"""
def write_to_zipfile(zipped_file: zipfile.ZipFile, dir_name: str, arc_name: str)-> zipfile.ZipFile:

    with zipped_file.open(zipped_file.namelist(), "w"):
        if os.path.isfile(dir_name):
            zipped_file.write(dir_name, arc_name)
        else:
            for item in zipped_file
    return zipped_file
"""


class ChangeHandler(FileSystemEventHandler):
    latestModifiedTime = 0.0
    bufferTimeSec = 10

    def on_modified(self, event: FileSystemEvent):
        print("modified at " + event.src_path)
        if abs(self.latestModifiedTime - time.time()) < ChangeHandler.bufferTimeSec:
            print("zipping was buffered.")
            return
        self.latestModifiedTime = time.time()
        print("time: " + str())
        time.sleep(0.1)
        _zip_specified_directory()
        shutil.make_archive(BASE_ZIP_NAME, "zip")
        print("zipped")


if __name__ in '__main__':
    _zip_specified_directory()
    print("zipped")
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, DIR_TO_WATCH)
    observer.start()
    while True:
        time.sleep(0.1)
