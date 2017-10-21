#访问字典的方法：keys(),values(),items()
dict3={}
dict3=dict3.fromkeys(range(32),'赞')
print(dict3)

print(dict3.get(31))
print(dict3.get(32))

print('1================')
dict4=dict3
print(dict4)


dict3.clear() #。clear()方法会把原字典清空的话，也会把赋值过的字典也会清空
print(dict3)
print(dict4)

print('2====================')

dict5={1:'one',2:'two',3:'three'}

dict6=dict5
print(dict6)

dict5={} #通过{}方法把原字典清空不会把赋值过的字典清空的,和之前列表切片不一样
print(dict5)
print(dict6)

print('3-----------------------------3')
#拷贝
a={1:'one',2:'two',3:'three'}
b=a.copy()
c=a
print(id(a)) #
print(id(b))#拷贝得到的字典地址和原字典地址不一样
print(id(c))#赋值得到的字典地址和原字典地址一样，和原来字典指向同一个对象



