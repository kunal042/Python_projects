import random

top_of_range = input("Type a Number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Type a number larger than 0 next time.")
        quit()
else:
    print("Please Type a number next time.")
    quit()

guesses = 0
random_number = random.randint(0, top_of_range)
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!!")
        break
    elif user_guess > random_number:
            print("You have guess greater number!")
    else:
        print("you have guess lesser number")

print(f"You got it in {guesses} guesses")


