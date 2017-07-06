from string import Template

template = '''
package $package;

import $superType;
import $mapperType;
import $modelType;
import $interfaceType;
import org.springframework.stereotype.Service;

/**
 * $comment
 */
@Service
public class $className extends $superClass<$modelName, $mapperName> implements $interfaceName {
}
'''


def get_content(params):
    t = Template(template)
    return t.substitute(params)
