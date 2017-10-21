
#property()通过属性设置属性

class C:
    def __init__(self,size=0):
        self.size=size

    def getSize(self):
        return self.size

    def setSize(self,value):
        self.size=value

    def delSize(self):
        del self.size

    x=property(getSize,setSize,delSize)

c1=C()
print(c1.getSize())
print(c1.x)

c1.x=18 #这里它调用的是property第二个设置参数的方法setSize()
print(c1.x)
print(c1.getSize())
