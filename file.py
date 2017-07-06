import os
import shutil


def clear_path(path):
    filelist = os.listdir(path)
    for f in filelist:
        filepath = os.path.join(path, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)


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


