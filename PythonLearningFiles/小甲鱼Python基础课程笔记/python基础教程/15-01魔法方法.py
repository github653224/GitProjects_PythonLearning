'''
#模仿方法总是被双下划线包围，如：__init__
魔法方法是面向对象的Python的一切
'''

#对基类str方法进行重写

class CapStr(str):
    def __new__(cls, string):     #对基类进行重写必须调用调用__new__方法
        string=string.upper()
        return str.__new__(cls,string)

a=CapStr('i love fishc.com')

print(a)