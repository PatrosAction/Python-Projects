import random 
import string

char = list(string.ascii_letters +string.digits + "!@#$%^&*()")
def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    random.shuffle(char)
    password = []
    for x in range(password_length):
        password.append(random.choice(char))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)
    
option = input("Do you wanna generate a pass? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("end")
    quit()
else:
    print("Invalid")
    quit()


