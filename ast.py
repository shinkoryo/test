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



=========================================================================================
# 参照リンク　 
# https://github.com/ivan111/vpyast/blob/master/main.py
from _ast import AST
import ast
import json
import ruamel.yaml


def ast2json(node):
    if not isinstance(node, AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    def _format(node):
        
        if isinstance(node, AST):
            fields = [('PyType', _format(node.__class__.__name__))]
            fields += [(a, _format(b)) for a, b in ast.iter_fields(node)]
            if node._attributes:
                fields.extend([(a, _format(getattr(node, a))) for a in node._attributes])

            return '{ %s }' % ', '.join(('"%s": %s' % field for field in fields))

        if isinstance(node, list):
            return '[ %s ]' % ', '.join([ _format(x) for x in node])

        return json.dumps(node)


    return _format(node)

node = ast.parse(Monster)
obj = json.loads(ast2json(node))

yml = ruamel.yaml.YAML()
with open('out_yaml3.yml', 'w', encoding = 'utf-8') as stream:
    yml.dump(obj, stream)
    
 ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
import ast
import json
import yaml
import ruamel.yaml
from _ast import AST
from collections import OrderedDict

class Visitor(ast.NodeVisitor):
    dump = []
    
    def visit_Name(self, node, data= None):

        if data:
            for field in node._fields:
                val = getattr(node, field)

                if isinstance(val, list):
                    for l in val:
                        self.visit_vame(l)
                else:
                    data[field] = val
            
        self.generic_visit(node)

    def visit_Import(self, node):
        print(node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        name = node.__class__.__name__
        data = OrderedDict()
        data[name] = OrderedDict()

        for field in node._fields:
            val = getattr(node, field)
    
            if isinstance(val, AST):
                print("ATS", val)
            elif isinstance(val, list):
                for l in val:
                    self.visit_alias(l, data[name])
            else:
                data[name][field] = val
        self.dump.append(data)
                
        self.generic_visit(node)

    def visit_alias(self, node, data=None):
        if data:
            temp = {}
            name = 'names'
            
            if name not in data:
                data[name] = []
            
            for field in node._fields:
                val = getattr(node, field)
                if isinstance(val, list):
                    for l in val:
                        self.visit_vame(l)
                else:                    
                    temp[field] = val

            data[name].append(temp)
        
        self.generic_visit(node)


SOURCE = """
from test.lib import libAAA
from test.lib2 import libBBB, libCCC
"""

if __name__ == "__main__":
    root = ast.parse(SOURCE)
    visitor = Visitor()
    visitor.visit(root)
    
    print(ast.dump(root))
    print()
    print(visitor.dump)
    print()
#     print(json.dumps(visitor.dump))
    
    yml = ruamel.yaml.YAML()
    with open('test.yaml', 'w', encoding = 'utf-8') as stream:
        yml.dump(visitor.dump, stream)
   
===================================================================================
# ################
# ver 3

import ast
import json
import yaml
import ruamel.yaml
from _ast import AST


class Visitor(ast.NodeTransformer):
    def __init__(self):
        self.dump = []
        self.body = None

    def init(self, node):
        self.name = node.__class__.__name__
        self.data = {}
        
        
        
    def set_dump(self, data):
        self.dump = data

    def dump_data(self, node, data):
        print('===========================================')
        print('view_node  ', node)
        print('view_data  ', data)
        print('view_dump  ', self.dump)
#         for v in self.dump:
#             if isinstance(v, AST):
#                 if v , node
#             if isinstance(v, list):
                
                
#             if isinstance(v, dict):
                
        lst = [v if node != v else data for v in self.dump]
        self.set_dump(lst)
        
    def make_data(self, node):
        name = node.__class__.__name__
        data = {}
        data[name] = {}
        
        for field, value in ast.iter_fields(node):
            if field not in ['level']:
                data[name][field] = value

        return data

            

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        
        if node.__class__.__name__ == 'Module':
            self.body = node.body
            self.dump = node.body

        if node in self.body:
            self.init(node)
        
        return visitor(node)
    
#     def visit_Name(self, node, data= None):

#         if data:
#             for field in node._fields:
#                 val = getattr(node, field)

#                 if isinstance(val, list):
#                     for l in val:
#                         self.visit_vame(l)
#                 else:
#                     data[field] = val
            
#         self.generic_visit(node)

#     def visit_Import(self, node):
#         print(node)
#         self.generic_visit(node)

    def visit_ImportFrom(self, node):

        data = self.make_data(node)

        self.dump_data(node, data)                
        self.generic_visit(node)

    def visit_alias(self, node, data=None):

        name = node.__class__.__name__
        data = self.make_data(node)

        self.dump_data(node, data[name])                
        self.generic_visit(node)


SOURCE = """
from test.lib import libAAA
from test.lib2 import libBBB, libCCC
"""

if __name__ == "__main__":
    root = ast.parse(SOURCE)
    visitor = Visitor()
    visitor.visit(root)
    
    print()
    print(ast.dump(root))
    print()
    print(visitor.dump)
    print()
    print(yaml.dump(visitor.dump, sort_keys=False))
    
#     yml = ruamel.yaml.YAML()
#     with open('test.yaml', 'w', encoding = 'utf-8') as stream:
#         yml.dump(json.loads(json.dumps(visitor.dump)), stream)


###################################################
###################################################
###################################################
# ################
# ver 3

import ast
import json
import yaml
import ruamel.yaml
from _ast import AST


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.dump = []
        self.body = None

    def init(self, node):
        self.name = node.__class__.__name__
        self.data = {}

        
    def exchange_data(self, node, data, dump):
        
        if isinstance(dump, list):
            for i, v in enumerate(dump):
                
                if isinstance(v, AST) and v == node:
                    dump[i] = data
                self.exchange_data(node, data, v)
                
        if isinstance(dump, dict):
            for k, v in dump.items():
                if isinstance(v, AST) and v == node:
                    dump[k] = data
                self.exchange_data(node, data, v)

    def make_data(self, node):
        name = node.__class__.__name__
        data = {}
        data[name] = {}
        
        for field, value in ast.iter_fields(node):
            if field not in ['level', 'ctx']:
                data[name][field] = value
        if node._attributes:
            for a in node._attributes:
                if a == 'lineno':
                    data[name][a] = getattr(node, a)
#             fields.extend([(a, _format(getattr(node, a))) for a in node._attributes])

        return data
    
#     def decorator(func):
#         def inner(self, *args, **kwargs):
#             func(self, *args, **kwargs)
#             name = node.__class__.__name__
#             data = {}
#             data[name] = {}
        
#             for field, value in ast.iter_fields(node):
#                 if field not in ['level', 'cxt']:
#                     data[name][field] = value
#             print(data)
#         return inner

            

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        
        if node.__class__.__name__ == 'Module':
            self.body = node.body
            self.dump = node.body

        if node in self.body:
            self.init(node)
        
        return visitor(node)
    
    def visit_Num(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Str(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_FormattedValue(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_JoinedStr(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Bytes(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_List(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Tuple(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Set(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Dict(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Ellipsis(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_NameConstant(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Name(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Load(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Store(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Del(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Starred(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Expr(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_UAdd(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_USub(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Not(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Invert(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_BinOp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Add(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Sub(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Mult(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Div(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_FloorDiv(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Mod(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Pow(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_LShift(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_RShift(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_BitOr(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_BitXor(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_BitAnd(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_MatMult(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_And(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Or(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Compare(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Eq(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_NotEq(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Lt(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_LtE(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Gt(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_GtE(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Is(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_IsNot(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_In(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_NotIn(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Call(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_keyword(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_IfExp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Subscript(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Index(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Slice(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_ExtSlice(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_ListComp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_SetComp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_DictComp(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_comprehension(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Assign(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Print(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Raise(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Assert(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Delete(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Pass(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Import(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)


    def visit_ImportFrom(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_alias(self, node):
        name = node.__class__.__name__
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump) 
        self.generic_visit(node)

    def visit_If(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_For(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_While(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Break(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Continue(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Try(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_TryFinally(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_TryExcept(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_With(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_withitem(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Lambda(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_arguments(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_arg(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Return(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Yield(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_YieldFrom(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Global(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Nonlocal(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_Await(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_AsyncFor(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)

    def visit_AsyncWith(self, node):
        data = self.make_data(node)

        self.exchange_data(node, data, self.dump)
        self.generic_visit(node)


SOURCE = """
from test.lib import libAAA

class MyClass(object):
    def __init__(self):
        self.my_var = "my_var"

    def decorator(func):
        def inner(self, *args, **kwargs):
            print(prefunc)
            print(self.my_var)
            func(self, *args, **kwargs)
            print(after_func)
        return inner

    @decorator
    def print_hoge(self, *args, **kwargs):
        print("hoge")


"""

if __name__ == "__main__":
    root = ast.parse(SOURCE)
    visitor = Visitor()
    visitor.visit(root)
    
    print()
    print(ast.dump(root))
    print()
    print(visitor.dump)
    print()
    print(yaml.dump(visitor.dump, sort_keys=False))
    
#     yml = ruamel.yaml.YAML()
#     with open('test.yaml', 'w', encoding = 'utf-8') as stream:
#         yml.dump(json.loads(json.dumps(visitor.dump)), stream)


###################################################################
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('arg')
    args = parser.parse_args()

    filename = args.arg

    with open(filename, 'r', encoding='utf-8') as f:
        source = f.read()

        root = ast.parse(source)
        visitor = Visitor()
        visitor.visit(root)

    print()
    print(ast.dump(root))
#     print()
#     print(visitor.dump)
#     print()
#     print(yaml.dump(visitor.dump, sort_keys=False))

#     with open('test.yaml', 'w', encoding = 'utf-8') as f:
#         yaml.dump(visitor.dump, f)

###################################################################
#　フォルダ作成
import pathlib
import glob
import re
import os

dir = r"C:\Work\83.Dev\test\python\GlobalFactor\src"
p_temp = pathlib.Path(dir).rglob('*')

# lst = glob.glob(dir, recursive = True)
lst = [str(p) for p in p_temp if p.is_dir()]
lst = [l.replace("C:\\Work\\83.Dev\\test\\python\\GlobalFactor", ".") for l in lst]
# lst = [re.sub(r"\\*.py", "", l) for l in lst]
print(lst)

for l in lst:
    os.makedirs(l)


###################################################################
#　YAML作成
import glob
import re
import os

dir = r"C:\Work\83.Dev\test\python\GlobalFactor\src\**\*.py"

lst = glob.glob(dir, recursive = True)
# lst = [l.replace("C:\\Work\\83.Dev\\test\\python\\GlobalFactor", ".").replace(".py", ".yaml") for l in lst]
# lst = [re.sub(r"\\*.py", "", l) for l in lst]

for l in lst:
    filename = l
    out_filename = l.replace("C:\\Work\\83.Dev\\test\\python\\GlobalFactor", ".").replace(".py", ".yaml")
    print(filename)
    print(out_filename)
    
    with open(filename, 'r', encoding='utf-8') as f:
        source = f.read()

    root = ast.parse(source)
    visitor = Visitor()
    visitor.visit(root)

#     print(ast.dump(root))

    with open(out_filename, 'w', encoding = 'utf-8') as f:
        yaml.dump(visitor.dump, f)


        
##########################################################
ドットで属性にアクセスするとき、Attributeノードで表します。
例えば；

・class Attribute(value, attr, ctx)
snake.colour

・class Call(func, args, keywords, starargs, kwargs)
funcの値を表したいとき
monster.howl()

・class Assign(targets, value, type_comment)
aのvalueにアクセスしたいとき
test = a.value

・class AnnAssign(target, annotation, value, simple)
aのvalueにアクセスしたいとき
a.value: int

・class AugAssign(target, op, value)
aのvalueにアクセスしたいとき
r += a.value

[リンク] https://greentreesnakes.readthedocs.io/en/latest/nodes.html#Attribute
