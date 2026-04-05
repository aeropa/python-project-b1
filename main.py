import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number (1-100)!")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("Rock, Paper, Scissors! (type 'quit' to exit)")
    
    while True:
        player = input("Your choice: ").lower()
        if player == "quit":
            break
        if player not in choices:
            print("Invalid choice. Try again.")
            continue
        
        computer = random.choice(choices)
        print(f"Computer: {computer}")
        
        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")


def dice_roll():
    print("Dice Roller! Roll two dice (type 'quit' to exit)")
    
    while True:
        roll = input("Press Enter to roll (or 'quit'): ")
        if roll.lower() == "quit":
            break
        
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"Roll: {die1} + {die2} = {total}")


def coin_flip():
    print("Coin Flip! (type 'quit' to exit)")
    
    while True:
        guess = input("Heads or Tails? ").lower()
        if guess == "quit":
            break
        if guess not in ["heads", "tails"]:
            print("Invalid choice.")
            continue
        
        result = random.choice(["heads", "tails"])
        print(f"Result: {result}")
        
        if guess == result:
            print("You win!")
        else:
            print("You lose!")


def higher_lower():
    print("Higher or Lower! Guess if next number is higher or lower (type 'quit' to exit)")
    
    while True:
        current = random.randint(1, 100)
        guess = input(f"Current number: {current}. Higher or Lower? ").lower()
        if guess == "quit":
            break
        if guess not in ["higher", "lower"]:
            print("Invalid choice. Type 'higher' or 'lower'.")
            continue
        
        next_num = random.randint(1, 100)
        print(f"Next number: {next_num}")
        
        if (guess == "higher" and next_num > current) or (guess == "lower" and next_num < current):
            print("You win!")
        elif next_num == current:
            print("Tie!")
        else:
            print("You lose!")


def number_tournament():
    print("Number Tournament! Guess the number in 7 attempts (type 'quit' to exit)")
    
    while True:
        number = random.randint(1, 100)
        max_attempts = 7
        won = False
        
        for attempt in range(1, max_attempts + 1):
            guess = input(f"Attempt {attempt}/{max_attempts}. Your guess: ")
            if guess.lower() == "quit":
                break
            
            guess = int(guess)
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"You got it! The number was {number}.")
                won = True
                break
        
        if not won and guess.lower() != "quit":
            print(f"Out of attempts! The number was {number}.")


def random_password():
    import string
    print("Password Generator! (type 'quit' to exit)")
    
    while True:
        length = input("Password length (or 'quit'): ")
        if length.lower() == "quit":
            break
        try:
            length = int(length)
            if length < 4:
                print("Length must be at least 4.")
                continue
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"Generated password: {password}")
        except ValueError:
            print("Please enter a valid number.")


def show_menu():
    print("\n=== Game Menu ===")
    print("1. Guess the Number")
    print("2. Rock Paper Scissors")
    print("3. Dice Roll")
    print("4. Coin Flip")
    print("5. Higher or Lower")
    print("6. Number Tournament")
    print("7. Password Generator")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select a game: ")
        
        if choice == "1":
            guess_number()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            dice_roll()
        elif choice == "4":
            coin_flip()
        elif choice == "5":
            higher_lower()
        elif choice == "6":
            number_tournament()
        elif choice == "7":
            random_password()
        elif choice == "8":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

