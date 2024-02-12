print("Welcome to my computer quiz! ")

playing = input("Do you want to play? : ")
  
if playing.lower() != "yes":
    print("if you want to play quiz type 'yes' ")
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "cental processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for?  ")
if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does RAM stand for?  ")
if answer.lower() == "random acsess memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')


answer = input("What does PSU stand for?  ")
if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print('Incorrect')
    

print(f"You got {score} question correct!!")
print(f"You got {(score/ 4)*100} %")
