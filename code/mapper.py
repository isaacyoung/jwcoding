from string import Template

template = '''
package $package;

import $superType;
import $modelType;

/**
 * $comment
 */
public interface $className extends $superClass<$modelName> {
}
'''


def get_mapper(params):
    t = Template(template)
    return t.substitute(params)
