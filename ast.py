import ast
import yaml
from ast import *
from pprint import pprint
Monster ="""
from ast import dump
class Monster:
    # ドキュメント作成
    def __init__(self):
        self.level=0
        self.hp=1000
        self.boom=[x for x in range(10)]
    def eat(self,frut):
        self.hp+=1
    def howl(self):
        print("Ao uuuuuuuuuuuuuu")
def test(test_a, test_b):
    print(test_a + test_b)
    
monster=Monster()
monster.howl()
"""

# cm = compile(Monster, '<string>', 'exec')
# exec (cm)
tree = ast.parse(Monster)

out_filename = "output.yaml"
yaml_dump = yaml.dump(tree, allow_unicode=True)
with open(out_filename, mode = 'w', encoding = 'utf-8') as f:
    f.write(yaml_dump)
    
def remove_letter(lst, *args):
    for arg in args:
        lst =  [key for key in lst if arg not in key]
    return lst

def replace_letter(lst, *args):
    for k, v in args:
        lst = [s.replace(k, v) for s in lst]
    return lst   

indent = ' '
include_attributes = False
annotate_fields = True
def _format(node, level=0):
    if isinstance(node, AST):
        fields = [(a, _format(b, level)) for a, b in iter_fields(node)]
        if include_attributes and node._attributes:
            fields.extend([(a, _format(getattr(node, a), level))
                           for a in node._attributes])
        return ''.join([
            node.__class__.__name__,
            ':\n',
            '\n'.join(((indent * (level + 2)) + '%s: %s' % field for field in fields)
                       if annotate_fields else
                       (b for a, b in fields)),
            ''])
    elif isinstance(node, list):
        lines = ['']
        lines.extend((indent * (level + 2) + _format(x, level + 2) + ''
                     for x in node))
        if len(lines) > 1:
            lines.append(indent * (level + 1) + '')
        else:
            lines[-1] += '[]'
        return '\n'.join(lines)
    return repr(node)

x_format = _format(tree)
print(x_format)

lst = x_format.splitlines()
string = remove_letter(lst, 'ctx:', 'body:', ': Name:', ': arguments:')
string = [a for a in string if len(a.lstrip()) > 0]
string


###################################
###################################
###################################
load checked
import ast
import yaml
import ruamel.yaml

yml = ruamel.yaml.YAML()

# yml_lod = yml.load(yaml.dump(tree))
# yml_lod


yaml_dump = yaml.dump(tree)
lst = yaml_dump.splitlines()

lst = remove_letter(lst, 'ctx:', 'state:', 'col_offset:', 'level:', 'lineno:')
string = '\n'.join(lst)

yml = ruamel.yaml.YAML()

yml_lod = yml.load(string)
# x = yml.dump(yml_lod)

with open('out_ruamel.yml', 'w', encoding = 'utf-8') as stream:
    yml.dump(yml_lod, stream=stream)
    
###################################
###################################
###################################

import ast
import json
import yaml
import ruamel.yaml

def remove_str(lst, *args):
    for arg in args:
        lst =  [key for key in lst if arg not in key]
    return lst

def insert_str(lst):
    i = 0
    string = '- !!python/object/apply:_ast.'
    str_list = [(i, v.replace(string, '  ') + ':') for i, v in enumerate(lst) if string in v]
    
    for index_no, value in str_list:
        lst.insert(index_no + i + 1, value)
        i += 1
    return lst

def replace_str(lst, *args):
    for k, v in args:
        lst =  [(s + ':').replace(k, v) if k in s else s.replace(k, v) for s in lst]
    return lst   


tree = ast.parse(Monster)
string = '!!python/object/apply:_ast.Module\n  body:\n'

dump = yaml.dump(tree)
lst = dump.splitlines()
lst = remove_str(lst, 'ctx:', 'state:', 'col_offset:', 'level:', 'lineno:', 'op: ')
lst = insert_str(lst)

string = '\n'.join(lst)
yml = ruamel.yaml.YAML()

output_dict = json.loads(json.dumps(yml.load(string)))

with open('out_yaml.yml', 'w', encoding = 'utf-8') as stream:
    yml.dump(output_dict, stream)    
    

    
——————————————————————————————————————————————————————————————————————————————

from collections import OrderedDict
import yaml

def ordered_yaml_load(yaml_path, Loader=yaml.Loader,
                      object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    with open(yaml_path) as stream:
        return yaml.load(stream, OrderedLoader)


def ordered_yaml_dump(data, filename, Dumper=yaml.SafeDumper):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())
            
    ## 这里是 把 生成文件里的 “null” 转为 “”
    def represent_none(self,_):        
     	return self.represent_scalar('tag:yaml.org,2002:null','')

    stream = None
    with open(filename, "w") as stream:
        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        OrderedDumper.add_representer(type(None), represent_none)
        yaml.dump(data,
                  stream,
                  OrderedDumper,
                  default_flow_style=False,
                  encoding='utf-8',
                  allow_unicode=True)
 
 
 ###  使用 
kv_conf_tmpl = ordered_yaml_load("./kkkk.conf")
ordered_yaml_dump(kv_conf_tmpl, "./after_kk.conf")
