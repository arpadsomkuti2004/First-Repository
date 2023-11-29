print("Welcome to my computer quiz! In this game you're going to answer to question about the PC hardware. ")

playing = input("Do you want to play? Write yes if you want to. ")

if playing.lower() != "yes": 
    quit()
    
print("Okay! Let's play!)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was: central processing unit. ")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer was: graphics processing unit. ")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer was: random access memory. ")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer was: power supply. ")

print("You got " + str(score) + " out of the 4 questions correct which is " + str ((score / 4) * 100) + "%. out of 100%.")
