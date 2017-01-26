import random


def point_system(n):
    if n == 1:
        points = 1280
        return points
    elif n == 2:
        points = 640
        return points
    elif n == 3:
        points = 320
        return points
    elif n == 4:
        points = 160
        return points
    elif n == 5:
        points = 80
        return points
    elif n == 6:
        points = 40
        return points
    elif n == 7:
        points = 20
        return points
    elif n == 8:
        points = 10
        return points

totalPoints = 0
cont = 'Y'
print('Welcome player! What is thy name? ')
playerName = raw_input()
print "Well", playerName, " let's play a numbers guessing game"
while cont == 'Y':
    computerNumber = random.randint(1, 100)
    totalGuesses = 0
    print (
    "I will think of a number between 1 and 100 and you have to guess it in atleast 8 tries, the sooner you get it right the more points you recieve")
    while totalGuesses != 8:
        playerNumber = input("Guess the number: ")
        totalGuesses += 1
        if playerNumber == computerNumber:
            totalPoints += point_system(totalGuesses)
            print "Good job! you got ",point_system(totalGuesses)," for guessing the right number in ",totalGuesses, " tries"
            cont = raw_input("Do you want to continue? Y/N").upper()
            if cont != 'Y':
                break
            break

        elif playerNumber > 100:
            print("What a waste of a guess... i said between 1 and 100")
        elif playerNumber < 0:
            print("What a waste of a guess... i said between 1 and 100")
        elif playerNumber > computerNumber:
            print "Nope the correct number is lower"
        elif playerNumber < computerNumber:
            print("Nope the correct number is higher")
        if totalGuesses == 8:
            print("Game Over, The number was: ", computerNumber)
            cont = raw_input("Do you want to continue? Y/N").upper()
            if cont != 'Y':
                break

print playerName, "got", totalPoints, "points"
