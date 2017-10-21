#issubclass()函数，检查第一个参数类是否是第二个参数类的子类
class A:
    pass
class B(A):
    pass

print(issubclass(B,A)) #检查B类是否是A类的子类，返回boolean类型的值
print(issubclass(B,object))

#hasattr(object,name)检查某个对象里是否有这个属性,第二个参数必须为字符

class C:
    def __init__(self,x=0):
        self.x=x

c1=C()
print(hasattr(c1,'x'))

print(getattr(c1,'x'))

print(getattr(c1,'y','您所访问的属性不存在'))#如果y属性不存在会提示我们设置的提示信息


print(setattr(c1,'y','您所访问的属性添加进去了'))
print(getattr(c1,'y'))

print(delattr(c1,'y'))
print(getattr(c1,'y','有被删除了'))












