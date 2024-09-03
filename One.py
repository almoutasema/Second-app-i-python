import random

def play_game():
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0
    max_attempts = 5  # Set the maximum number of attempts

    print("Welcome to the guessing game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")

    # Game loop
    while attempts < max_attempts:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess < number_to_guess:
                print("The number you entered is too low. Try again.")
            elif guess > number_to_guess:
                print("The number you entered is too high. Try again.")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

    if guess != number_to_guess:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
