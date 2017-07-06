import os
import shutil


def clear_path(path):
    shutil.rmtree(path)


def create_path(path):
    os.makedirs(path)


def create_file(file, content):
    path = file[:file.rfind(os.sep)]
    if not os.path.exists(path):
        create_path(path)

    f = open(file, 'w')
    f.write(content)
    f.flush()
    f.close()


