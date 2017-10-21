#在Python中定义私有变量只需要在变量名或者函数名上加上"__"两个
#下划线，那么这个函数或者变量就会为私有的了
'''
class Person:
    name='小甲鱼'

p=Person()
print(p.name) #小甲鱼,这里可以访问

'''

# class Person:
#     __name='小甲鱼'
#
# p=Person()
# print(p.name) #这里会报错：AttributeError: 'Person' object has no attribute 'name'
#类中没有这个属性，原因是把他私有化,隐藏了，所以是无法访问的
class Person:
    __name='小甲鱼'
    def getName(self):
        return self.__name

p=Person()

print(p.getName())  #可以通过在类内部定义一个方法，这个方法来在类内部返回这个私有的属性就可间接访问
t=p._Person__name#还可以通过他来访问，其实私有化后，会把__name隐藏在_Person__name中
print(t)

#Python的类时没有访问权限控制的，和其他语言不一样

