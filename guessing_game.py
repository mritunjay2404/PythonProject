import random
winning_number = random.randint(1,100)
guess = 1
guessed_number = int(input("Enter the winning number between 1 - 100 : "))
game_over=False
while not game_over:
    if winning_number==guessed_number:
        print(f"YOU WIN.... and you guessed in {guess} time..")
        game_over = True
    else:
        if guessed_number<=winning_number:
            print("you guessed TOO LOW..")
            guess += 1
            guessed_number  = int(input("Enter number again..:"))
        else:
            print("You guessed TOO HIGH..")
            guess += 1
            guessed_number  = int(input("Enter number again..:"))