# auto code

import os
import file
from code import mapper
from config import Config

if os.path.isdir(Config.get_prop('target.path')):
    file.clear_path(Config.get_prop('target.path'))

# mapper
mapper_path = Config.get_prop('target.path') + os.sep + Config.chage_to_path(Config.get_prop('package.dao'))
mapper_file = mapper_path + os.sep + 'TestMapper.java'
mapper_content = mapper.get_mapper()
file.create_file(mapper_file, mapper_content)
