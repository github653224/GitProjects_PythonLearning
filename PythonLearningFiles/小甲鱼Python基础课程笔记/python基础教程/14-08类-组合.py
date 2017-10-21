class Turtle:
    def __init__(self,x):
        self.num=x

class Fish:
    def __init__(self,y):
        self.num=y

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)      #重点,这里没哟进行继承，但是可以横向组合达到纵向继承的效果
#组合就是把类的实例放在新的类里面，通过对新类实例化来调用旧类的实例的过程二达到继承的效果
    def pirnt_num(self):
        print('水池里共有乌龟%d只，小鱼%d条'% (self.turtle.num,self.fish.num))

p=Pool(1,10)
p.pirnt_num()

