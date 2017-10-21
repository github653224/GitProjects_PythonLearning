"""score=int(input("enter your score:"))
if score>=90 and score <=100:
    print("A")
if 90>score>=80:
    print("B")
if 80>score>=60:
    print("C")
if 60>score>=0:
    print("不及格")
if score<0 or score>100:
    print("输入错误")
"""
score=int(input("enter your score:"))
if 100>=score>=90:
    print("A")
elif 90>score>=80:
    print("B")
elif 80>score>= 60:
    print("C")
elif score>=0 and score<60:

    print("D")
else:
    print("输入错误")

#三元操作符
x,y=4,5
if x<y:
    small=x
else:
    small=y

print(small)
print("==========================")

small=x if x<y else y #三元操作符

print(small)




















