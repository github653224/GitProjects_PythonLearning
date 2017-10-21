num1={1,2,3,4,5,5,6,6} #集合会把重复的去掉保留一个
print(num1)
print(1 in num1)

num1.add(7)
print(num1)

num1.remove(1)
print(num1)

#定义一个不可变的集合：不可删除和不可增加

num3=frozenset([1,2,3,4,5,10,90])
print(num3)

print(num3.add(100))#报错，因为我们申请是一个frozenset集合不可变的