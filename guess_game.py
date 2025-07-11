import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess the number between 1 and 100")

while True:
    try:
        guess = int(input("👉 Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("🔻 Too low! Try again.")
        elif guess > secret_number:
            print("🔺 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
            break
    except ValueError:
        print("⚠️ Please enter a valid number.")
