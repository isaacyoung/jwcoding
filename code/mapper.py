from string import Template

template = '''
package com.cdsq.manage.pro.dao;

import com.cdsq.manage.base.BaseMapper;
import com.cdsq.manage.pro.domain.BArea;

/**
 * 
 */
public interface BAreaMapper extends BaseMapper<BArea> {
}
'''


def get_mapper():
    t = Template(template)
    return t.substitute()
