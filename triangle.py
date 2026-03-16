import time
import random
delay = random.randint(2, 5)

def calculator(number):
    while True:
        try:
            value = float(input(number))

            if value <= 0:
                raise ValueError("Input must be a positive number")

            return value

        except ValueError:
            print("Try again.")

a = calculator("Enter the length of the first side: ")
b = calculator("Enter the length of the second side: ")
c = calculator("Enter the length of the third side: ")

print("Currently Calculating... you have slow internet")
time.sleep(random.randint)

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle is real")
else:
    print("The triangle is not real")
