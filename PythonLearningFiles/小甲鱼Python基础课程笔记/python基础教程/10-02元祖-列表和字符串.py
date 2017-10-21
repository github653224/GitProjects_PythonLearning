#元祖tuple()元祖是不可以改变的列表
tuple1=(1,2,3,4,5,6,7,8)
print(tuple1)

print(tuple1[1])
print(tuple1[:])

print(tuple1[5:])

#注意定义一个元素的元祖，小括号里必须有逗号,

tuple2=(2,)#或者 tuple2=2,
print(type(tuple2))

#也可以这样声明

tuple3=3,5,6
print(type(tuple3))

#跟新和删除元祖 删除用del
temp=('小甲鱼','迷途','怡静','小布丁')
print(temp)

temp=temp[:2]+('嘿嘿',)+temp[2:]
print(temp)


