def FunX(x):
    def FunY(y):
        return x*y
    return FunY

i=FunX(8)
print(i) #<function FunX.<locals>.FunY at 0x0054C6A8>

print(type(i))#<class 'function'>

s=i(9)
print(s)#72

print('====================')
b=FunX(6)(6)
print(b) #36



print('-----------------------------------------')

"""
def Fun1():
    x=5
    def Fun2():
        x *= x
        return x
    return Fun2()    #这里调用会出错，原因x=5对fun2()函数来说在它的函数体外也是不能进行修改的

"""

def Fun1():
    x=5
    def Fun2():
        nonlocal x  #加上这个就不出错了，声明x不是局部变量
        x *= x
        return x
    return Fun2()