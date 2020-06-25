arg 下の　arg 下の　posonlyargとはなんですか？とはなんですか？
argumentsの引数になります。python3.8で追加された。

arg 下の　type_commentとはなんですか？
https://greentreesnakes.readthedocs.io/en/latest/nodes.html#Assign

classAssign(targets, value, type_comment)
classFor(target, iter, body, orelse, type_comment)
classWith(items, body, type_comment)
classFunctionDef(name, args, body, decorator_list, returns, type_comment)
classarg(arg, annotation, type_comment)
classAsyncFunctionDef(name, args, body, decorator_list, returns, type_comment)


https://docs.python.org/ja/3/library/typing.html

constant:

NameConstant:
https://docs.python.org/ja/3/library/ast.html
バージョン 3.8 で変更: :class:`ast.Constant`が全ての定数に使われるようになりました。
バージョン 3.8 で非推奨: ast.Num、 ast.Str、ast.Bytes、ast.NameConstant そして ast.Ellipsis は現バージョンまで使用可能ですが、将来のPythonリリースで削除される予定です。削除されるまでの間、これらをインスタンス化すると、異なるクラスのインスタンスが返されます。


===========================================================================
make_data
""" dumpリストにデータを格納する
    nodeの属性を{node.name:{keys:values}}型式で、dumpリストに格納する処理

"""

visit_Attribute
""" dumpリストにデータを格納する
    Attributeノードの属性を{Attribute:{keys:values}}型式で、dumpリストに格納する処理

"""
