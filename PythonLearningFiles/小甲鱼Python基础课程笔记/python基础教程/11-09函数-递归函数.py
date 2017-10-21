"""
def fact(n):
    result=1
    for i in range(1,n):
        result*=i
    return result

number=int(input('请输入一个正整数：'))
print(fact(number))

"""
#递归缺点
def fact1(n):
    if n==1:
        return 1
    else:
        return n*fact1(n-1)

number=int(input('请输入一个正整数：'))
print(fact1(number))