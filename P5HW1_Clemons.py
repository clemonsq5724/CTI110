# CTI-110 
 # P5HW1 - Math Quiz
 # Clemons
 # 11/12/2023


import random

def add_numbers():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    print(num1)
    print("+", num2)
    total = num1 + num2
    user_answer = int(input("Enter the answer: "))
    num_guesses = 1
    while user_answer != total:
        if user_answer < total:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        user_answer = int(input("Enter the answer: "))
        num_guesses += 1
    print("Congratulations! You got it in", num_guesses, "guesses.")

def subtract_numbers():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    print(num1)
    print("-", num2)
    total = num1 - num2
    user_answer = int(input("Enter the answer: "))
    num_guesses = 1
    while user_answer != total:
        if user_answer < total:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        user_answer = int(input("Enter the answer: "))
        num_guesses += 1
    print("Congratulations! You got it in", num_guesses, "guesses.")

def main():
    choice = 0
    while choice != 3:
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_numbers()
        elif choice == 2:
            subtract_numbers()

main()