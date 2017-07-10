# auto code
# python jwcoding.py
# python jwcoding.py [table] [-m]
# [-m] copy(move) to project source

import os

import sys

import connection
import file
from code import mapper, service, serviceimpl, model, mapperxml
from config import Config
from model import tableutils


args = sys.argv
over = False
if len(args) == 1:
    tables = connection.get_tables()
else:
    for a in args:
        if a == '-m':
            over = True
        else:
            tables = connection.get_table(args[1])


if os.path.exists(Config.get_prop('target.path')):
    file.clear_path(Config.get_prop('target.path'))

# mapper
for t in tables:
    mapper_file = tableutils.get_mapper_file(t[0])
    params = {
        'package': Config.get_prop('package.dao'),
        'className': tableutils.get_java_mapper_name(t[0]),
        'superType': 'com.cdsq.manage.base.BaseMapper',
        'superClass': 'BaseMapper',
        'modelType': Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(t[0]),
        'modelName': tableutils.get_java_model_name(t[0]),
        'comment': t[1]
    }
    mapper_content = mapper.get_content(params)
    file.create_file(mapper_file, mapper_content)

# service
for t in tables:
    service_file = tableutils.get_service_file(t[0])
    params = {
        'package': Config.get_prop('package.serv'),
        'className': tableutils.get_java_service_name(t[0]),
        'superType': 'com.cdsq.manage.base.BaseService',
        'superClass': 'BaseService',
        'modelType': Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(t[0]),
        'modelName': tableutils.get_java_model_name(t[0]),
        'comment': t[1]
    }
    service_content = service.get_content(params)
    file.create_file(service_file, service_content)

# service impl
for t in tables:
    service_impl_file = tableutils.get_service_impl_file(t[0])
    params = {
        'package': Config.get_prop('package.serv') + '.impl',
        'className': tableutils.get_java_service_impl_name(t[0]),
        'superType': 'com.cdsq.manage.base.BaseServiceImp',
        'superClass': 'BaseServiceImp',
        'modelType': Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(t[0]),
        'modelName': tableutils.get_java_model_name(t[0]),
        'mapperType': Config.get_prop('package.dao') + '.' + tableutils.get_java_mapper_name(t[0]),
        'mapperName': tableutils.get_java_mapper_name(t[0]),
        'interfaceType': Config.get_prop('package.serv') + '.' + tableutils.get_java_service_name(t[0]),
        'interfaceName': tableutils.get_java_service_name(t[0]),
        'comment': t[1]
    }
    service_impl_content = serviceimpl.get_content(params)
    file.create_file(service_impl_file, service_impl_content)

# model
for t in tables:
    model_file = tableutils.get_model_file(t[0])
    params = {
        'package': Config.get_prop('package.model'),
        'className': tableutils.get_java_model_name(t[0]),
        'content': model.get_column_content(t[0]),
        'comment': t[1]
    }
    model_content = model.get_content(params)
    file.create_file(model_file, model_content)

# mapper xml
for t in tables:
    columns = connection.get_columns(t[0])
    mapper_xml_file = tableutils.get_mapper_xml_file(t[0])
    params = {
        'mapperType': Config.get_prop('package.dao') + '.' + tableutils.get_java_mapper_name(t[0]),
        'resultMap': mapperxml.get_result_map(t[0], columns),
        'baseColumn': mapperxml.get_base_column_list(),
        'selectById': mapperxml.get_select_by_id(t[0], columns),
        'deleteById': mapperxml.get_delete_by_id(t[0], columns),
        'select': mapperxml.get_select(t[0], columns),
        'insert': mapperxml.get_insert(t[0], columns),
        'update': mapperxml.get_update(t[0], columns),
        'delete': mapperxml.get_delete(t[0], columns)
    }
    mapper_xml_content = mapperxml.get_content(params)
    file.create_file(mapper_xml_file, mapper_xml_content)

if over:
    file.move_to_project()

