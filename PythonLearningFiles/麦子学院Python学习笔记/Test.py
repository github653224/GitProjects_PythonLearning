class TestCss:
    cssa='class-attribute'
    #类属性定义在类体内方法之外，调用时用类名.调用
    def __init__(self):
        self.a=0
        self.b=10
    def info(self):
        print('a:' ,self.a, 'b:',self.b,'cssa:',TestCss.cssa)

    def define_a(self):
        self.c=19

if __name__=='__main__':
    # tc=TestCss()
    # tc.info() #a: 0 b: 10  a:0 b:10
    # tc.color='red' #  red 很少在类外进行绑定属性一般在类内
    # print(tc.color)


    # tc=TestCss()
    # tca=TestCss()
    # tc.a=100
    # tc.b=200
    # tc.info()#a: 100 b: 200
    # tca.info() #a: 0 b: 10    #同一个累的不同实例对象的属性值不一样

    # tc=TestCss()
    # tc.define_a()
    # print(tc.c) #如果在这之前不调用该犯法的话会出错，原因我们没有在AttributeError: 'TestCss' object has no attribute 'c'

    tc=TestCss()
    tc.info()  #a: 0 b: 10 cssa: class-attribute

    tca=TestCss()
    tca.info() #a: 0 b: 10 cssa: class-attribute

    TestCss.cssa=0 #在类体外对类属性进行修改

    tcc=TestCss()
    tcc.info()

    tc.info()
    tca.info()