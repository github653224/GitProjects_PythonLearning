class A:
    def __init__(self):
        self.__ab=0     #双下划线
    def info(self):
        print(self.__ab)
a=A()
a.info()#0

a.__ab=3
a.info()#0
# #发现没有对私有属性__ab修改成功，原因是__ab前加了爽下划线
#是属于私有属性，不能在类外进行修改，但是类对象可以访问
#但是下面输出可以
print(a.__ab) #3
# 这是因为我们在类外对私有属性__ab进行修改时
#Python会在类外也创建另外一个__ab变量和类里面的不一样

print(A.__doc__)
print(A.__dict__)
print(A.__name__)
print(A.__module__)
print(A.__base__)
