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


def show_menu():
    print("\n=== Game Menu ===")
    print("1. Guess the Number")
    print("2. Rock Paper Scissors")
    print("3. Dice Roll")
    print("4. Coin Flip")
    print("5. Exit")


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
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

