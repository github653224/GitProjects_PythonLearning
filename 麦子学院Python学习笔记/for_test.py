number=59
num_chaces=3
print("your chances is "+ str(num_chaces)+"\ttimes")

for i in (1,(num_chaces+1)):

    print("chance "+str(i))
    guess=int(input("enter your luck NO.:"))
    if guess==number:
        print("you guessed it rightly !")
        break
    elif guess<number:
        print("your NO. is small "+"you have "+str(num_chaces-i)+" chance left")
    else:
        print("your NO. is big "+"you have "+str(num_chaces-i)+" chance left")

print("done")