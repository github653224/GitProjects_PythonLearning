class Parent():
    def hello(self):
        print('在调用父类的方法')
'''
class Child(Parent):#子类继承父类，也会继承其方法
    pass

p=Parent()
p.hello()

c=Child()
c.hello() #子类中并没有hello()方法但是可以调用，原因是子类继承了父类的方法

'''

class Child(Parent):
    def hello(self):
        print('在调用子类的方法') #方法重写

c=Child()
c.hello()
