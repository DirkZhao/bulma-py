#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:48
# @Author  : Dirk Zhao

import yaml


class Person(yaml.YAMLObject):
    yaml_tag = '!Person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person(%s,%s)' %(self.name, self.age)


lebron = Person('lebron', 33)
print (yaml.dump(lebron))


def person_repr(dumper, data):
    return dumper.represent_mapping(u'!person', {"name": data.name, "age": data.age})


yaml.add_representer(Person, person_repr)
print (yaml.dump(lebron))


def person_cons(loader, node):
    value = loader.construct_mapping(node)
    name = value['name']
    age = value['age']
    return Person(name, age)


yaml.add_constructor(u'!Person', person_cons())