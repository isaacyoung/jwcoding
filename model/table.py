
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
    if table.find('_') != -1:
        temp = table.split('_')
        for s in temp:
            s.capitalize()
        return temp.join('')
    else:
        return temp.capitalize()

