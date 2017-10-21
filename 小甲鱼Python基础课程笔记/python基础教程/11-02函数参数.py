#函数参数分为形参和实参
#函数文档

def MyFirstFunction():
    """
    这里的是函数文档
    """

# print(MyFirstFunction.__doc__)#调用函数的文档
# print(help(MyFirstFunction))#调用函数的文档

#关键字参数
def say(name,words):
    print(name+'->'+words)

say('小甲鱼','让编程改变世界')
say(words='让Python改变世界',name='panxueyan')

#默认值参数
def say2(name='zhangsan',words='让编程改变生活'):
    print(name+'->'+words)

say2()
say2('lisi')
say2(words='让代码改变世界')

print('1===================================')

def test(*params): #传很多个参数
    print('参数的长度是：',len(params))
    print('第二个参数时：',params[1])

test(1,'小甲鱼',3.14,5,6,7,8)

print('2=====================================')

def test2(*params,exp): #传很多个参数
    print('参数的长度是：',len(params),exp)
    print('第二个参数时：',params[1])

test2(1,'小甲鱼',3.14,5,6,7,exp=8)