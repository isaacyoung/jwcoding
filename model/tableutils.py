
def get_java_model_name(table):
    return get_java_class_name(table)


def get_java_mapper_name(table):
    return get_java_model_name(table) + 'Mapper'


def get_java_service_name(table):
    return get_java_model_name(table) + 'Service'


def get_java_service_impl_name(table):
    return get_java_service_name(table) + 'Impl'


def get_java_class_name(table):
    temp = table
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
