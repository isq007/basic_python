
import random   # Import the random module

# Generate a random number between 1 and 20
random_number = random.randint(1, 20)

guess_count = 0
max_guesses = 5

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 20. You have 5 attempts to guess it.")

while guess_count < max_guesses:
    try:
        # Accept user input
        user_guess = int(input("Enter your guess (1-20): "))

        # Validate input range
        if user_guess < 1 or user_guess > 20:
            print("Invalid input! Please enter a number between 1 and 20.")
            continue  # Ask again without counting this as an attempt

        guess_count += 1  # Increment guess count

        # Check the guess
        if user_guess < random_number:
            print("Too Low")
        elif user_guess > random_number:
            print("Too High")
        else:
            print("Correct! You guessed the number in", guess_count, "attempt(s).")
            break  # Exit loop if guessed correctly

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# If user fails to guess in 5 attempts
if guess_count == max_guesses and user_guess != random_number:
    print("Game Over! The correct number was", random_number)
