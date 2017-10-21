number=59
guess_flag=False

while guess_flag==False:
    guess=int(input("please enter your luck NO.:"))
    if guess==number:
        print("congratulation, you had got your NO.")
        guess_flag=True
    elif guess<number:
        print("sorry, your NO. is samll")
    else:
        print("sorry , your NO. is big")

print("haha  you right")
