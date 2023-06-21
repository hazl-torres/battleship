import random
import numpy
oceanGrid = numpy.zeros([10, 10])
battleships = [(5, 4), (4, 3), (3, 2), (2, 2), (1, 1)]

# Build Ocean Grid
for ship, numShips in battleships:
    compass = ["left", "right", "up", "down"]
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    direction = random.choice(compass)
    if oceanGrid[row, col] == 0:
        oceanGrid[row, col] = ship
    else:
        while oceanGrid[row, col] != 0:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
        oceanGrid[row, col] = ship
    condition1 = list(range(0, numShips))
    condition2 = list(range(10-numShips, 10))

    # Remove direction at borders
    if row in condition1:
        compass.remove("up")
    if row in condition2:
        compass.remove("down")
    if col in condition1:
        compass.remove("left")
    if col in condition2:
        compass.remove("right")

    # Check for overlap
    for i in range(numShips):
        if "left" in compass:
            if oceanGrid[row, col-i-1] != 0:
                compass.remove("left")
        if "right" in compass:
            if oceanGrid[row, col+i+1] != 0:
                compass.remove("right")
        if "up" in compass:
            if oceanGrid[row-i-1, col] != 0:
                compass.remove("up")
        if "down" in compass:
            if oceanGrid[row+1+i, col] != 0:
                compass.remove("down")

    direction = random.choice(compass)
    match direction:
        case "left":
            for i in range(numShips):
                oceanGrid[row, col-i-1] = ship
        case "right":
            for i in range(numShips):
                oceanGrid[row, col+i+1] = ship
        case "up":
            for i in range(numShips):
                oceanGrid[row-i-1, col] = ship
        case "down":
            for i in range(numShips):
                oceanGrid[row+i+1, col] = ship

# Build Target Grid
targetGrid = numpy.empty([11, 11], dtype="<U2")
targetGrid[0, 0] = "-"
for i in range(1, 11):
    targetGrid[0, i] = i
for i in range(1, 11):
    targetGrid[i, 0] = i
for i in range(1, 11):
    for j in range(1, 11):
        targetGrid[i, j] = "-"
print("Welcome to battleship!")
print(oceanGrid)
print(targetGrid)
count5 = 0
count4 = 0
count3 = 0
count2 = 0
count1 = 0

while count5 != 5 or count4 != 4 or count2 != 3 or count2 != 3 or count1 != 2:
    row_guess = 0
    while row_guess not in list(range(1, 11)):
        try:
            row_guess = input("Row: ")
            if row_guess == "q" or row_guess == "Q":
                break
            else:
                row_guess = int(row_guess)
            if row_guess not in list(range(1, 11)):
                print("Please enter a valid row number between 1-10. Press q to quit")
        except:
            print("Please enter a valid row number between 1-10. Press q to quit")
            continue
    if row_guess == "q" or row_guess == "Q":
        print(oceanGrid)
        print("You Lose!")
        break
    col_guess = 0
    while col_guess not in list(range(1, 11)):
        try:
            col_guess = input("Column: ")
            if col_guess == "q" or col_guess == "Q":
                break
            else:
                col_guess = int(col_guess)
            if col_guess not in list(range(1, 11)):
                print("Please enter a valid row number between 1-10. Press q to quit")
        except:
            print("Please enter a valid column number between 1-10. Press q to quit")
            continue
    if col_guess == "q" or col_guess == "Q":
        print("You Lose!")
        print("OceanGrid")
    if oceanGrid[row_guess-1, col_guess-1] == 0:
        targetGrid[row_guess, col_guess] = "X"
        print("Miss!")
    if oceanGrid[row_guess-1, col_guess-1] == 1 and targetGrid[row_guess, col_guess] != "O":
        targetGrid[row_guess, col_guess] = "O"
        print("Hit!")
        count1 += 1
        if count1 == 2:
            print("You have sunk the Destroyer!")
    if oceanGrid[row_guess-1, col_guess-1] == 2 and targetGrid[row_guess, col_guess] != "O":
        targetGrid[row_guess, col_guess] = "O"
        print("Hit!")
        count2 += 1
        if count2 == 3:
            print("You have sunk the Submarine!")
    if oceanGrid[row_guess-1, col_guess-1] == 3 and targetGrid[row_guess, col_guess] != "O":
        targetGrid[row_guess, col_guess] = "O"
        print("Hit!")
        count3 += 1
        if count3 == 3:
            print("You have sunk the Cruiser")
    if oceanGrid[row_guess-1, col_guess-1] == 4 and targetGrid[row_guess, col_guess] != "O":
        targetGrid[row_guess, col_guess] = "O"
        print("Hit!")
        count4 += 1
        if count4 == 4:
            print("You have sunk the Battleship")
    if oceanGrid[row_guess-1, col_guess-1] == 5 and targetGrid[row_guess, col_guess] != "O":
        targetGrid[row_guess, col_guess] = "O"
        print("Hit!")
        count5 += 1
        if count5 == 5:
            print("You have sunk the Carrier")
    print(targetGrid)
if count5 == 5 and count4 == 4 and count2 == 3 and count2 == 3 and count1 == 2:
    print("CONGRATULATIONS, YOU WIN!")