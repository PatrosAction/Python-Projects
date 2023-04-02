import random

top_of_range = input("type of number: " )

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print("plz type a number larger than 0 next time")
        quit()
else:
    print("plz type a number next time")
    quit()
         
random_number = random.randint(0,top_of_range)
quesses =0
while True:
    quesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("plz type a number next time")
        continue #bring us back to the very top of our loop
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess>random_number:
            print("You were above the number!")
        else:
            print("You were below the number")
        
print("you git it in",quesses,"quesses")
    
    
# r = random.randint(11)
# r = random.randrange(-1,11)
#print(r)