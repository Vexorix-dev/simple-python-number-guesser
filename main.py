import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print("A random number between 1 and 100 has been generated. Guess the number.")

# Initialize user_guess with a dummy value
user_guess = -1  

# Keep asking the user until they guess correctly
while user_guess != random_number:
    try:
        user_guess = int(input("Enter your guess (1-100): "))
        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
        elif user_guess > random_number:
            print("The random number is lower than your answer. Try again.")
        elif user_guess < random_number:
            print("The random number is higher than your answer. Try again.")
        else:
            print("Great job! You guessed correctly!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


