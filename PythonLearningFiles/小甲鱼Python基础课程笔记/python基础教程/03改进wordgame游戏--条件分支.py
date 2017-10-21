print("----------------python练习------------------")
temp = input("不放猜下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
n=2
while guess !=8 and n!=0:                      
    temp = input("猜错了，请重新输入试一试：")
    guess = int(temp)
    n=n-1

    if guess == 8:
        print("我操，你是小甲鱼肚子里的蛔虫吗")
        print("哼，猜中了也没哟奖励")
    else:
        if guess > 8:
            print("大了，再输一次")
        if guess < 8:
            print("小了，再次输一次")

print("游戏结束，不玩啦")