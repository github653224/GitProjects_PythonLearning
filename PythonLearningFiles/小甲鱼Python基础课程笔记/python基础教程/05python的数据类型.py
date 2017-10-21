#整形、浮点型、布尔类型、e记法
# e记法

print(1.5e4) #1.5*10*10*10*10
#类型转换
a="520"
print(a)

b=int(a)
print(b)

print(int(5.99))#浮点型转换为整数型时，会把小数点后面的砍掉，不会四舍五入的

print(float(520))

print(str(5.99999999))

#获取类型的信息typeof
print("\n")
c="480"
print(type(c))

print("\n")
a="小甲鱼"
b=100
print(isinstance(a,str))
print(isinstance(a,int))
print(isinstance(b,int))
print(isinstance(b,float))



