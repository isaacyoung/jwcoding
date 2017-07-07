from string import Template

import connection
from model import columnutils

template = '''
package $package;

/**
 * $comment
 */
public class $className {
    $content
}
'''

field = '''
    /** $comment */
    private $type $name;
'''

get_method = '''
    public $type $name() {
        return $field;
    }
'''

set_method = '''
    public void $name($type $temp) {
        this.$field = $temp;
    }
'''


def get_content(params):
    t = Template(template)
    return t.substitute(params)


def get_column_content(t):
    columns = connection.get_columns(t)
    result = ''
    for column in columns:
        t = Template(field)
        result += t.substitute({"type": columnutils.get_java_type(column[3]),
                                "name": columnutils.get_java_field_name(column[1]),
                                "comment": column[6]})

    for column in columns:
        t = Template(get_method)
        result += t.substitute({
            "name": columnutils.get_java_get_method_name(column[1]),
            "field": columnutils.get_java_field_name(column[1]),
            "type": columnutils.get_java_type(column[3])
        })
        t = Template(set_method)
        result += t.substitute({
            "name": columnutils.get_java_get_method_name(column[1]),
            "field": columnutils.get_java_field_name(column[1]),
            "type": columnutils.get_java_type(column[3]),
            "temp": '_' + columnutils.get_java_field_name(column[1])
        })

    return result
