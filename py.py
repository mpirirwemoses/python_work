average = 50

guess = int(input("Enter Your Guess: "))

while guess != average:
    if guess > average:
        print("very high")
    elif guess < average:
        print("very low")
    guess = int(input("Enter Your Guess: "))

print("correct")
