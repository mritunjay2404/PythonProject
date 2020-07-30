winning_number = int(45)
guessed_number = int(input("Enter the winning number"))
if winning_number==guessed_number:
    print("YOU WIN....")
else:
    if guessed_number<=winning_number:
        print("you guessed TOO LOW..")
    else:
        print("You guessed TOO HIGH..")
