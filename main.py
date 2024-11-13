import random

def guess_the_number():
    print("welcome to the guess the number im thinking of game!")
    level = 1
    score = 0
    
    while True:
        print(f"\n--- Level {level} ---")
        max_number = level * 10
        number_to_guess = random.randint(1, max_number)
        attempts = max(5 - level // 2, 1)
        
        print(f"I'm thinking of a number between 1 and {max_number}.")
        print(f"You have {attempts} attempts to guess it.")

        for attempt in range(attempts):
            try:
                guess = int(input(f"Attempt {attempt + 1}/{attempts}: Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            if guess == number_to_guess:
                print("Congratulations! You guessed the number.")
                points = (attempts - attempt) * 10
                score += points
                print(f"You earned {points} points. Total score: {score}")
                break
            elif guess < number_to_guess:
                print("Higher!")
            else:
                print("Lower!")
        else:
            print(f"Out of attempts! The number was {number_to_guess}.")
            break

        level += 1

    print(f"\nGame Over! Your final score is: {score}")
    
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye!")

guess_the_number()