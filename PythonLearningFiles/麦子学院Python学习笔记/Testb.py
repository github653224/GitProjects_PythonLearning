class A:
    def __init__(self):
        self._ab=0     #单下划线没有什么限制性的作用
    def info(self):
        print(self._ab)
a=A()
a.info()#0

a._ab=3
a.info()#3
print(a._ab) #3
