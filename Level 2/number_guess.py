import random

def number_guesser_game():
    print("Welcome to the Number Guessing Game!")
    
   
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"I have picked a number between {lower_bound} and {upper_bound}.")
    print("Try to guess the number!")

    while True:
        try:
            
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guesser_game()
