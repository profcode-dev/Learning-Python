# Explain the game to the user 
Explain = """ This game is to Guess a number and I will tell you if it even or odd \n"""
print(Explain)

# import modules
import random

# welcome message
name = input("Enter your name: ")
print(f"Hi {name.title()}!")


while True:
    try: 
        # عمل المعادلة 
        print('Guess a number!')
        value = int(input())
        res = value % 2 

        if res == 0 : 
            print('this is even')
        elif res != 0:
            print('this is odd')
            
        # شرط الخروج من البرنامج    
        ques = input('Do you want to continue (y/n): ')
        if ques != 'y':
            break
    except ValueError:
        print('Give me a valid number')
    print("---------------------------------------")