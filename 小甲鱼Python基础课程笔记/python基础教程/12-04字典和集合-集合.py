num={}
print(type(num)) #<class 'dict'>

num1={1,2,3,4,5} #这只有键没有值，键和值没有一一对应，就不是字典了,而是集合<class 'set'>
print(type(num1)) #<class 'set'>

#在集合的世界里你就是我的唯一
#创建集合的方法有两个：
# 1、一种是直接把一对元素用花括号括起来
# 2、一种是使用set()工厂函数创建
set1=set([1,2,3,4,5,5,6,6])
print(set1) #集合会把重复的数字去掉保留一个，和数学中的自合亦一样


temp=[]
for each in set1:
    if each not in temp:
        temp.append(each)

print(temp)

num2={9}
