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

if __name__ == "__main__":
    guess_number()

