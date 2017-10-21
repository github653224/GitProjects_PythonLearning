import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x -=1
        print('我的位置是：',self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self) #利用父类调用其构造方法---未绑定的父类方法也可以用super()
        super().__init__()
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃')
            self.hungry=False
        else:
            print('太撑了，迟不了了')

fish=Fish()
fish.move()

goldfish=Goldfish()
goldfish.move()

shark=Shark()
shark.eat()
shark.eat()

# Fish.__init__(shark)
# shark.move() #报错，重写了父类的方法故调用不了，
#
# # 要想访问就要在子类构造方法中加入：Fish.__init__(self) #利用父类调用其构造方法
shark.move()