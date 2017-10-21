import os
import requests
print(os.getcwd())

# r=requests.get("https://www.baidu.com")
# print(r)
# print(r.url)

age=30
name="Tom"
print("{} is {} years old".format(name,age))
#Tom is 30 years old

# print(name+"is"+age+"years old")#这句有语法错误，Python中必须把非字符串的数字类型装换为字符串
print(name+"\tis\t"+str(age)+"\tyears old") #Tom	is	30	years old

s=list(range(1,10))
print(s)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(range(1,2)))#<class 'range'>

for i in range(1,10):
    print(i)           #1 2 3 4 5 6 7 8 9
print("===========1")

a_list=[1,3,"a",9]
for i in a_list:
    print(i)#13 a 9

print("===============2")

b_dict={"tom":"111","lily":"222","xiaoming":"333"}

for i in b_dict: #这里如果是一个参数，默认遍历的是字典的键不是值
    print(i) #lily xiaoming tom

print("================3")
for i in b_dict: #这里如果是一个参数，默认遍历的是字典的键不是值
    print(i)
    print(b_dict[i])  #根据遍历的是字典的键，把这个键传入字典就可以把其值也遍历出来
"""
lily
222
xiaoming
333
tom
111"""

print("======================4")

for i ,k in b_dict.items():#这里带上字典的items方法，且遍历的参数为2个的话，第一个为键，第二个为值
    print(i,k)
"""
lily 222
xiaoming 333
tom 111
"""


