# auto code

import os

import connection
import file
from code import mapper
from config import Config
from model import tableutils

if os.path.exists(Config.get_prop('target.path')):
    file.clear_path(Config.get_prop('target.path'))

tables = connection.get_tables()

# mapper
mapper_path = Config.get_prop('target.path') + os.sep + Config.chage_to_path(Config.get_prop('package.dao'))
for t in tables:
    mapper_file = mapper_path + os.sep + tableutils.get_java_mapper_name(t[0]) + '.java'
    params = {
        'package': Config.get_prop('package.dao'),
        'className': tableutils.get_java_mapper_name(t[0]),
        'superType': 'com.cdsq.manage.base.BaseMapper',
        'superClass': 'BaseMapper',
        'modelType': Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(t[0]),
        'modelName': tableutils.get_java_model_name(t[0]),
        'comment': t[1]
    }
    mapper_content = mapper.get_mapper(params)
    file.create_file(mapper_file, mapper_content)
