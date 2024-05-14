from lark import Transformer
from quack_ast import Add, Assign, Call, Div, Mul, Number, Sub, Var


#将parser生成的parse tree转换成AST
class QuackTransformer(Transformer):
    def assignment(self, items):
        var = str(items[0])
        vartype = str(items[1])
        expr = items[2]
        return Assign(var, vartype, expr)
    
    def add(self, items):
        left = items[0]
        right =items[1]
        return Add(left, right)
    
    def sub(self, items):
        left = items[0]
        right =items[1]
        return Sub(left, right)
    
    def mul(self, items):
        left = items[0]
        right =items[1]
        return Mul(left, right)
    
    def div(self, items):
        left = items[0]
        right =items[1]
        return Div(left, right)
    
    def call(self,items):
        obj = items[0]
        method = str(items[1])
        args = items[2:]
        return Call(obj, method, args)
    
    def var(self, items):
        return Var(str(items[0]))
    
    def number(self, items):
        return Number(int(items[0]))
    
    def expr(self, items):
        return items[0]
