import zipfile
import time
import os
from pathlib import Path

DIR_TO_WATCH = "C:/Users/Sango/PycharmProjects/AWSLambdaSample/"
DIR_TO_PUBLISH = "D:\AWSZips/"
BASE_ZIP_NAME = "ZipSandBox"
DIR_TO_ARCHIVE = "C:/Users/Sango/PycharmProjects/AWSLambdaSample/"

if __name__ in '__main__':
    zipped_file = zipfile.ZipFile(
        os.path.join(DIR_TO_PUBLISH, BASE_ZIP_NAME + str(int(time.time())) + ".zip"),
        "w",
        zipfile.ZIP_DEFLATED)
    zipped_file.write("C:/Users\Sango\PycharmProjects\AWSLambdaSample/requests", BASE_ZIP_NAME)
    path = Path(DIR_TO_ARCHIVE)
    for item_name in map(lambda x: str(x), list(path.glob("**/*"))):
        print(item_name)
        if "venv" not in str(item_name):
            zipped_file.write(item_name, os.path.relpath(item_name, DIR_TO_ARCHIVE))
    zipped_file.close()

    zipped_file.printdir()
