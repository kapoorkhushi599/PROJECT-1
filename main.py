import random
'''
1 for snake
-1 for water
0 for gun
'''
computer= random.choice([1,-1,0])
youstr= input("Enter your choice:    ")
youDict= {"S":1,"W": -1,"G": 0}
reverseDict = {1:"Snake",-1:"water",0:"gun"}

you= youDict[youstr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]} ")

if(computer==you):
    print("Its a draw!")
else:
     if(computer==1 and you==-1):
         print("you loose")
     elif(computer==1 and you==0):
         print("you win")
     elif(computer==-1 and you==1):
         print("you win")
     elif(computer==-1 and you==0):
         print("you loose")
     elif(computer==0 and you==1):
         print("You loose")
     elif(computer==0 and you==-1):
         print("You win")
     else:
        print("Something went Wrong!")



