print("welcome to my computer quiz! ")

playing = input("Do you want to play? ")


if playing != "yes":
    quit()
    
print("okay! Let's play ")
score =0


answer = input("What does CPU stand for?")
if answer.lower() == "centeral processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")


answer = input("What does GPU stand for?")
if answer == "graphics processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")



answer = input("What does RAM stand for?").lower()

if answer == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
    
answer = input("What does PSU stand for?")
if answer == "power supply unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)*100) + " %.")

