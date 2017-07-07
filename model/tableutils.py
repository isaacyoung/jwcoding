import os

from config import Config


def get_java_model_name(table):
    return get_java_class_name(table)


def get_java_mapper_name(table):
    return get_java_model_name(table) + 'Mapper'


def get_java_service_name(table):
    return get_java_model_name(table) + 'Service'


def get_java_service_impl_name(table):
    return get_java_service_name(table) + 'Impl'


def get_java_class_name(table):
    temp = table.lower()
    if temp.find('_') != -1:
        temp = temp.split('_')
        result = []
        for s in temp:
            result.append(s.capitalize())
        return ''.join(result)
    else:
        return temp.capitalize()


def get_short_name(name):
    return name[name.rfind('.')+1]


def get_mapper_file(table):
    return Config.get_prop('target.path') + os.sep + Config.chage_to_path(Config.get_prop('package.dao')) \
           + os.sep + get_java_mapper_name(table) + '.java'


def get_service_file(table):
    return Config.get_prop('target.path') + os.sep + Config.chage_to_path(Config.get_prop('package.serv')) \
           + os.sep + get_java_service_name(table) + '.java'


def get_model_file(table):
    return Config.get_prop('target.path') + os.sep + Config.chage_to_path(Config.get_prop('package.model')) \
           + os.sep + get_java_model_name(table) + '.java'


def get_service_impl_file(table):
    return Config.get_prop('target.path') + os.sep + Config.chage_to_path(Config.get_prop('package.serv')) \
           + os.sep + 'impl' \
           + os.sep + get_java_service_impl_name(table) + '.java'

