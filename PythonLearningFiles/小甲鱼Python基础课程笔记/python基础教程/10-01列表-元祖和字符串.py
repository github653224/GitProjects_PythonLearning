#列表

number1=['小甲鱼','小布丁','黑夜','迷途','怡静']
print(number1)

number2=[1,2,3,4,5]
print(number2)

mix=[1,'小甲鱼','3.14',[1,2,3]]
print(mix)

empty=[]
print(empty)
print("===列表的添加的方法：append()、extend()、insert(index,yuansu)====")

number2.append('福禄娃娃')  #append()的方法默认向列表最后添加一个元素
print(number2)

number2.extend([6]) #extend()的方法向列表中添加多个元素，但是它添加时是以列表的形式添加进去的
print(number2)

number2.extend([7,8,9]) #extend()的方法向列表中添加多个元素，但是它添加时是以列表的添加进去的
print(number2)

number3=[1,2,3]
print(number3)

number3.insert(0,10) #列表的insert()方法插入，第一个参数是指列表中的索引位置，第二个是指要插入的元素
print(number3)

print("===获取列表元素===")

number5=['小甲鱼','小布丁','黑夜','迷途','怡静']
s=number5[0]
print(s)    #获取小甲鱼这个元素，通过其对应的所以index(0)


print(number5)
temp=number5[0]
number5[0]=number5[1]
number5[1]=temp
print(number5)  #实现了列表里 小甲鱼 和 小布丁 的元素位置调换

print("===列表的删除的方法:pop(index)、remove('元素')、del list(index)===")
number4=['小甲鱼','怡静','小布丁','3.14',[1,2,3],44,90]
print(number4)

number4.remove('小甲鱼')
print(number4)

del number4[2]
print(number4)

print('===============列表分片==============================')

number6=['小甲鱼','怡静','小布丁','3.14',[1,2,3],44,90]
print(number6)
print(number6[1:3]) #分片的参数指的是索引，参数包左不包右，所以3.14没有分出来
print(number6[:])
print(number6[1:])
print(number6[:-1])

print('----------in / ont in------------------')
#in / ont in

list1=[1,3,6,'小甲鱼']
print(1 in list1)

print('小甲鱼' not in list1)

list2=[3,1,90,5,66,6,3]
print(list2.count(3)) #list2.count()方法计算在列表中3出现的次数

print(list2.index(66)) #list2.index()返回列表中元素所在的索引

list2.reverse() #reverse对列表进行翻转
print(list2)

list2.sort()
print(list2)  #对列表进行排序，从小到大排序


list3=[7,2,6,10,30,5]
print(list3)

list3.sort(reverse=True) #对列表进行从小到大排序后并且再进行翻转reverse=True为翻转，False为不翻转
print(list3)

list3.sort(reverse=False) #对列表进行从小到大排序后并且再进行翻转reverse=True为翻转，False为不翻转
print(list3)

























































