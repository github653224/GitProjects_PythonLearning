number=59
while True:
    guess=int(input('enter an integer:'))
    if guess == number:
        break  #break，执行到这一句的话，会结束整个循环，break后面的都不再执行且整个循环都不造不执行
    elif guess<number:
        print('No, the number is higher than that,keep guessing')
        continue #执行的到这一句时，这一句后面的语句都不再执行，条件不在做判断，直接跳到开始重新下一轮循环
    else:
        print('No, the number is a lower than that, keep guessing')
        continue

print("done")