#封装、继承、多态
class Turtle:
    color='green'
    weight=10
    legs=4
    shell=True
    mouth='大嘴'

    #ethods
    def climb(self):
        print('我在很努力的向前爬....')

    def run(self):
        print('我正在飞快的向前跑...')

    def bite(self):
        print('咬死你呀，咬死你呀')

    def eat(self):
        print('有的词，真满足...')
    def sleep(self):
        print('困了，睡了，晚安 Z z z')


Turtle().climb() #这个为类对象,没有引用指向它，会被垃圾回收器回收
a=Turtle()  #实例对象
a.climb()
a.sleep()