import random
target = random.randint(1,100)
while True :
    user_choice = input("Guess The Number Or Quit (Q) :- ").upper()
    if(user_choice == "Q"):
        break
    
    user_choice = int(user_choice)
    if(user_choice == target):
        print("Success : Correct Guess ")
        break
    elif (user_choice < target):
        print("Your Choice is less than target Take Bigger Guess")
        
    else :
        print("Your Choice is Too Big Take Smaller Guess")
        
print("------Game Over ------")