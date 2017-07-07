def get_java_field_name(column):
    temp = column.lower()
    if temp.find('_') != -1:
        temp = temp.split('_')
        result = []
        for s in temp:
            if len(result) == 0:
                result.append(s)
            else:
                result.append(s.capitalize())
        return ''.join(result)
    else:
        return temp


def get_java_get_method_name(column):
    temp = column.lower()
    if temp.find('_') != -1:
        temp = temp.split('_')
        result = []
        for s in temp:
            result.append(s.capitalize())

        return 'get' + ''.join(result)
    else:
        return temp


def get_java_set_method_name(column):
    temp = column.lower()
    if temp.find('_') != -1:
        temp = temp.split('_')
        result = []
        for s in temp:
            result.append(s.capitalize())

        return 'set' + ''.join(result)
    else:
        return temp


def get_jdbc_type(type):
    temp = type.upper()
    if temp =='INT':
        temp = 'INTEGER'
    return temp


def get_java_type(type):
    temp = type.upper()
    if temp == 'ARRAY':
        return 'Object'
    elif temp == 'BIGINT':
        return 'Long'
    elif temp == 'BINARY':
        return 'byte[]'
    elif temp == 'BIT':
        return 'Boolean'
    elif temp == 'BLOB':
        return 'byte[]'
    elif temp == 'BOOLEAN':
        return 'Boolean'
    elif temp == 'CHAR':
        return 'String'
    elif temp == 'CLOB':
        return 'String'
    elif temp == 'DATALINK':
        return 'Object'
    elif temp == 'DATE':
        return 'Date'
    elif temp == 'DECIMAL':
        return 'BigDecimal'
    elif temp == 'DISTINCT':
        return 'Object'
    elif temp == 'DOUBLE':
        return 'Double'
    elif temp == 'FLOAT':
        return 'Double'
    elif temp == 'INT':
        return 'Integer'
    elif temp == 'INTEGER':
        return 'Integer'
    elif temp == 'JAVA_OBJECT':
        return 'Object'
    elif temp == 'LONGVARBINARY':
        return 'String'
    elif temp == 'LONGVARCHAR':
        return 'byte[]'
    elif temp == 'NCHAR':
        return 'String'
    elif temp == 'NCLOB':
        return 'String'
    elif temp == 'NVARCHAR':
        return 'String'
    elif temp == 'LONGNVARCHAR':
        return 'String'
    elif temp == 'NULL':
        return 'Object'
    elif temp == 'NUMERIC':
        return 'BigDecimal'
    elif temp == 'OTHER':
        return 'Object'
    elif temp == 'REAL':
        return 'Float'
    elif temp == 'REF':
        return 'Object'
    elif temp == 'SMALLINT':
        return 'Short'
    elif temp == 'STRUCT':
        return 'Object'
    elif temp == 'TIME':
        return 'Date'
    elif temp == 'TIMESTAMP':
        return 'Date'
    elif temp == 'TINYINT':
        return 'Byte'
    elif temp == 'VARBINARY':
        return 'byte[]'
    elif temp == 'VARCHAR':
        return 'String'
    else:
        return 'Object'
