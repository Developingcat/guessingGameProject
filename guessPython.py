import random

def guessingGame():
    secret_number = random.randint (1, 100)
    attempts = 0 

    while True: 
        try:
            #Prompt the user for their guess 
            guess = int(input("Enter your guess:"))
            attempts += 1 

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100")
            elif guess < secret_number:
                print("Your guess is too low, try again.")
            elif guess > secret_number:
                print("Your guess is too high, please try again.")
            else: 
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input, please enter a whole number.")


if __name__  == "__main__":
    guessingGame()