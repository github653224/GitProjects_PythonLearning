#全局变量在函数体内和外都可以访问，但是在函数体内是无法对全局变量进行修改的
#局部变量只能在函数体内访问，出了函数就不能访问
#如果想在函数体内对全局变量进行修改就要在函数体内在全局变量前面加上：global
"""
count=5
def MyFun():
    count=10
    print(11)

MyFun() 11
print(count)#没有对全局变量进行修改成功 5

"""



count=5
def MyFun():
    global count  #声明count是全局变量
    count=10
    print(11)

MyFun()
print(count)#对全局变量进行修改成功 10

