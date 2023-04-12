name = input("What's your name? ")
print("Hi",name,"Welcome to this adventure ")

print(" ")
answer = input("You are on a dirt road, it has come to the end and you can go to the left or right.Which way would you like to go (left/right)? ")

if answer == "left":
    answer = input("you come to a river,there is a alert existing alligator. you can walk around it or swim across.So which one, walk or swim? ")
    
    
    if answer == "swim":
        print("You swam acrosses and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many milese, ran out of water and you found your way and you win")
    else:
        print("not a valid option.You lose. ")
    




elif answer == "right":
    answer = input("You come to the bridge, it looks wobbly, do you wanna cross it or head back (cross/back)? ")
     
    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet the stanger. Do you talk to them? (yes/no)? ")
        
            
        if answer == "yes":
            print("You talk to the stranger and they give you gold.You win.")
        elif answer == "no":
            print("You ignore the stanger and they are offended and you lose.")
        else:
            print("not a valid option.You lose. ")
      
    else:
        print("not a valid option.You lose. ")
        
        
else:
    print("not a valid option.You lose. ")