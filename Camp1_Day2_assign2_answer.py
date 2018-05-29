
from random import randint

print("Guess a number from 1 to 10. ")
print("")
num = randint(1,10)


while True:
    new_num = input("Guess the number: ")
    if new_num != str(num):
        print ("Wrong! Try again")

    else:
        print ("Correct!")
        break
