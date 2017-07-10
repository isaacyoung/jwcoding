from string import Template

from config import Config
from model import tableutils, columnutils

template = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="$mapperType">
$resultMap
$baseColumn
$selectById
$deleteById
$select
$insert
$update
$delete

</mapper>\
'''

result_map = '''\
  <resultMap id="BaseResultMap" type="$type">
$content
  </resultMap>\
'''

result_map_content = '''    <$tag column="$name" jdbcType="$type" property="$field" />'''

base_column_list = '''
  <sql id="Base_Column_List">
    $content
  </sql>\
'''

select_by_id = '''
  <select id="selectById" parameterType="java.lang.Integer" resultMap="BaseResultMap">
    select * from $tableName
    $where
  </select>\
'''

delete_by_id = '''
  <delete id="deleteById" parameterType="java.lang.Integer">
    delete from $tableName
    $where
  </delete>\
'''

select = '''
  <select id="select" parameterType="$parameterType" resultMap="BaseResultMap">
    select 
    <include refid="Base_Column_List" />
    from $tableName a
    <trim prefix="where" prefixOverrides="and|or">
$content
    </trim>
  </select>\
'''

insert = '''
  <insert id="insert" keyProperty="id" parameterType="$parameterType" useGeneratedKeys="true">
    insert into $tableName ($columns) 
    values
    <foreach collection="list" index="index" item="item" separator=",">
       $insertValues
    </foreach>
  </insert>\
'''

update = '''
  <update id="update" parameterType="$parameterType">
    <foreach close="" collection="list" index="index" item="item" open="" separator=";">
      update $tableName
      <set>
$content
      </set>
      $where
    </foreach>
  </update>\
'''

delete = '''
  <delete id="delete" parameterType="$parameterType">
    delete from $tableName
    <trim prefix="where" prefixOverrides="and|or">
$content
    </trim>
  </delete>\
'''


def get_content(params):
    t = Template(template)
    return t.substitute(params)


def get_result_map(table, columns):
    t = Template(result_map)
    return t.substitute({
        "type": Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(table),
        "content": get_result_map_content(columns)
    })


def get_result_map_content(columns):
    result = ''
    for i, c in enumerate(columns):
        if c[2] == 'PRI':
            tag = 'id'
        else:
            tag = 'result'

        t = Template(result_map_content)
        result += t.substitute({
            'tag': tag,
            'name': c[1],
            'type': columnutils.get_jdbc_type(c[3]),
            'field': columnutils.get_java_field_name(c[1])
        })
        if i != len(columns) -1:
            result += "\n"

    return result


def get_base_column_list():
    t = Template(base_column_list)
    return t.substitute({
        "content": 'a.*'
    })


def get_column_list(columns):
    content = ' '
    temp = ''
    for i, c in enumerate(columns):
        if len(temp) > 80:
            content += '\n     '
            temp = ''
        content += c[1]
        temp += c[1]

        if i != len(columns) - 1:
            content += ', '
            temp += ', '
    return content


def get_select_by_id(table, columns):
    t = Template(select_by_id)
    return t.substitute({
        "tableName": table,
        "where": get_where_key(columns)
    })


def get_delete_by_id(table, columns):
    t = Template(delete_by_id)
    return t.substitute({
        "tableName": table,
        "where": get_where_key(columns)
    })


def get_select(table, columns):
    t = Template(select)
    return t.substitute({
        "parameterType": Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(table),
        'tableName': table,
        'content': get_where_content(columns, ali='a.')
    })


def get_where_content(columns, prefix='', ali=''):
    result = ''
    for i, c in enumerate(columns):
        java_type = columnutils.get_java_type(c[3])
        java_name = columnutils.get_java_field_name(c[1])
        jdbc_type = columnutils.get_jdbc_type(c[3])
        if java_type == 'Integer' or java_type == 'Long' or java_type == 'Byte':
            result += '      <if test="' + prefix + java_name + ' != null and ' + prefix + java_name + ' !=  -1 ">\n'
        elif java_type == 'String':
            result += '      <if test="' + prefix + java_name + ' != null and ' + prefix + java_name + ' !=  \'\'">\n'
        else:
            result += '      <if test="' + prefix + java_name + ' != null ">\n'

        if i != 0:
            result += '        and ' + ali + c[1] + ' = #{' + prefix + java_name + ',jdbcType=' + jdbc_type + '}\n'
        else:
            result += '        ' + ali + c[1] + ' = #{' + prefix + java_name + ',jdbcType=' + jdbc_type + '}\n'
        result += '      </if>'
        if i != len(columns) - 1:
            result += '\n'
    return result


def get_insert(table, columns):
    t = Template(insert)
    return t.substitute({
        "parameterType": Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(table),
        'tableName': table,
        'columns': get_column_list(columns),
        'insertValues': get_insert_values(columns)
    })


def get_insert_values(columns):
    content = '('
    temp = ''
    for i, c in enumerate(columns):
        if len(temp) > 80:
            content += '\n        '
            temp = ''
        content += '#{item.' + columnutils.get_java_field_name(c[1]) + ',jdbcType=' + columnutils.get_jdbc_type(c[3]) + '}'
        temp += '#{item.' + columnutils.get_java_field_name(c[1]) + ',jdbcType=' + columnutils.get_jdbc_type(c[3]) + '}'
        if i != len(columns) - 1:
            content += ', '
            temp += ', '
    content += ')'
    return content


def get_update(table, columns):
    t = Template(update)
    return t.substitute({
        "parameterType": Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(table),
        'tableName': table,
        'content': get_update_content(columns, 'item.'),
        'where': get_where_key(columns, 'item.')
    })


def get_update_content(columns, prefix=''):
    result = ''
    for i, c in enumerate(columns):
        if c[2] == 'PRI':
            continue

        java_type = columnutils.get_java_type(c[3])
        java_name = columnutils.get_java_field_name(c[1])
        jdbc_type = columnutils.get_jdbc_type(c[3])
        if java_type == 'Integer' or java_type == 'Long' or java_type == 'Byte':
            result += '        <if test="' + prefix + java_name + ' != null and ' + prefix + java_name + ' !=  -1 ">\n'
        elif java_type == 'String':
            result += '        <if test="' + prefix + java_name + ' != null and ' + prefix + java_name + ' !=  \'\'">\n'
        else:
            result += '        <if test="' + prefix + java_name + ' != null ">\n'

        result += '          ' + c[1] + ' = #{' + prefix + java_name + ',jdbcType=' + jdbc_type + '}'
        if i != len(columns) - 1:
            result += ','
        result += '\n'
        result += '        </if>'
        if i != len(columns) - 1:
            result += '\n'
    return result


def get_delete(table, columns):
    t = Template(delete)
    return t.substitute({
        "parameterType": Config.get_prop('package.model') + '.' + tableutils.get_java_model_name(table),
        'tableName': table,
        'content': get_where_content(columns)
    })


def get_where_key(columns, prefix=''):
    result = ''
    where = False
    for c in columns:
        if c[2] is None or c[2] == '':
            continue
        if where:
            result += ' and '
        else:
            result += 'where '
            where = True

        result += c[1] + ' = #{' + prefix + columnutils.get_java_field_name(c[1]) + ',jdbcType=' + columnutils.get_jdbc_type(c[3]) + '}'

    return result
