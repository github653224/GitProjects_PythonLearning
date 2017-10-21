#Python类中函数中self指的是，类实例化后对象自身
class Ball:
    def setName(self,name):
        self.name=name

    def kick(self):
        print('我叫%s,该死的谁踢我' % self.name)

a=Ball()
a.setName('球A')
b=Ball()
b.setName('球B')
a.kick()
b.kick()