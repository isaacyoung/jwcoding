import os
import shutil

from config import Config


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

    f = open(file, 'w', encoding='utf-8')
    f.write(content)
    f.flush()
    f.close()


def move_to_project():
    from_path = Config.get_prop('target.path')
    to_path = Config.get_prop('project.path')

    to_java_path = to_path + Config.chage_to_path('.src.main.java.com')
    to_resource_path = to_path + Config.chage_to_path('.src.main.resources.mapper')

    if not os.path.exists(to_java_path):
        create_path(to_java_path)
    copy_files(from_path + os.sep + 'com', to_java_path)

    if not os.path.exists(to_resource_path):
        create_path(to_resource_path)
    copy_files(from_path + os.sep + 'mapper', to_resource_path)


def copy_files(source_dir, target_dir):
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)
        target_file = os.path.join(target_dir, file)
        if os.path.isfile(source_file):
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            if not os.path.exists(target_file) \
                    or (os.path.exists(target_file) and (os.path.getsize(target_file) != os.path.getsize(source_file))):
                open(target_file, "wb").write(open(source_file, "rb").read())
        if os.path.isdir(source_file):
            copy_files(source_file, target_file)
