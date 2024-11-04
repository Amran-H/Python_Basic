import random

Number = random.randint(1, 100)
print("Guess the number between 1 - 100")

for attempts in range(1, 1000):
    
    your_guess = int(input("Enter your guess: "))
    
    if your_guess == Number:
        print(f"Congratulations! You guessed the number  in {attempts} attempts")
    elif your_guess > Number:
        print("High! try again")
    elif your_guess < Number:
        print("Low! try again")



