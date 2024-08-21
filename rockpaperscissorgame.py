import random
i=1
totalscore=0
l=["rock","paper","scissor"]
while(i!=0):
    print("choose any one of the below")
    print("1.Rock\n2.paper\n3.Scissors")
    m=int(input())
    ran=random.randint(1,len(l))
    if(m==1):
        print(f"you have choosen rock")
        if(ran==1):
            print(f"computer have choosen {l[ran-1]}")
            print(f"it is a tie try again ")
            print(f"your total score is {totalscore}")   
        elif(ran==2):
            print(f"computer have choosen {l[ran-1]}")
            print("you lost man,try again")
            print(f"your total score is {totalscore}")
        elif(ran==3):
            print(f"computer have choosen {l[ran-1]}")
            print("you wonnn and got a point")
            totalscore+=1
            print(f"your total score is {totalscore}")
    elif(m==2):
        print(f"you have choosen paper")
        if(ran==2):
            print(f"computer have choosen {l[ran-1]}")
            print("it's a tie try againn")
            print(f"your total score is {totalscore}")
        elif(ran==1):
            print(f"computer have choosen {l[ran-1]}")
            print("Hurraaih you won and got a point")
            totalscore+=1
            print(f"your total score is {totalscore}")
        else:
            print(f"computer have choosen {l[ran-1]}")
            print("you lost man try again")
            print(f"your total score is {totalscore}")
    elif(m==3):
        print("you have choosen scissors")
        if(ran==1):
            print(f"computer have choosen {l[ran-1]}")
            print("you lost man try again")
            print(f"your total score is {totalscore}")
        elif(ran==2):
            print(f"computer have choosen {l[ran-1]}")
            print("you wonnn and got a point")
            totalscore+=1
            print(f"your total score is {totalscore}")
        elif(ran==3):
            print(f"computer have choosen {l[ran-1]}")
            print("it's a tie try againn")
            print(f"your total score is {totalscore}")
    else:
        print("make a valid choice mann!!!")
    i=int(input("do you want to continue:"))
print(f"your total score is {totalscore}")
print("the game ended..............")
print("Bye Bye Bye")