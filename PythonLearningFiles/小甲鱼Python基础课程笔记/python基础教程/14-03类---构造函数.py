#在Python的构造方法是：__init__(self):
class Ball:
    def __init__(self,name):
        self.name=name
    def kick(self):
        print('我叫%s,该死的谁踢我' % self.name)

b=Ball('土豆')
b.kick()

c=Ball() #这里会报错

