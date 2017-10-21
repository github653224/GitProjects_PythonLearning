class C:
    count=0

a=C()
b=C()
c=C()

print(a.count)#0
print(b.count)#0
print(c.count)#0  这三个都为实例对象

print('1================================')
c.count+=10    #实例属性把类属性覆盖了
print(c.count) #10
print(a.count)#0
print(b.count)#0

print('2===============================')
C.count+=100 #类对象
print(a.count)#100
print(b.count)#100
print(c.count)#10   #实例属性把类属性覆盖了