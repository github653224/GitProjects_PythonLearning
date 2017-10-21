#
print(type(len))#<class 'builtin_function_or_method'>
print(type(dir))#<class 'builtin_function_or_method'>
print(type(int))#<class 'type'>
print(type(list))#<class 'type'>

class C:
    pass
c=C()
print(type(C))#<class 'type'> #类对象也就是工程函数
print(type(c))#<class '__main__.C'>

a=int('123') #其实这个就是int（）类的实例化
print(a)