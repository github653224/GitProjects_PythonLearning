"""
while 条件：
     循环体

for 目标 in 表达式：（这里的表达式为列表）
    循环体

"""
myfavourite="fishc"
for i in myfavourite:
    print(i,end=" ")

print("\n")

number=["小甲鱼","小布丁","黑夜","迷途","逸静"]
for each in number:
    print(each,len(number))

#range()函数
v=range(5)#只有一个参数时，默认从0开始，生成5个整数从0开始：0,1,2,3,4
print(v)

v1=list(v)
print(v1)

c=range(2,9)#有两个参数时默认从第一个参数开始
print(list(c))

print("1==========================1")
for i in range(4,10):  #有2个参数
    print(i)

print("2---------------------------2")
for i in range(1,10,2):
    print(i)















