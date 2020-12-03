# Trying it out in python

# Read in file and take out new line issue
myFile = open("inputPuzzle3.txt")
UncleanLines = myFile.readlines()
TreeMap = []
for line in UncleanLines:
    TreeMap.append(line.strip())

# Counting Loop for Part 1
TreeCounter = 0
StepsAcross = 0
JumpNumber = 3
for row in TreeMap:
    if row[StepsAcross] == "#":
        TreeCounter = TreeCounter + 1
    
    StepsAcross  = StepsAcross + JumpNumber
    if StepsAcross > len(row[StepsAcross]):
        StepsAcross = StepsAcross - 31

print("The answer to part 1 is ", TreeCounter)

# Counting Loop for Part 2

TreeCounterRoute1 = 0
TreeCounterRoute2 = 0 
TreeCounterRoute3 = 0 
TreeCounterRoute4 = 0 
TreeCounterRoute5 = 0 

StepsAcrossRoute1 = 0
StepsAcrossRoute2 = 0 
StepsAcrossRoute3 = 0 
StepsAcrossRoute4 = 0 
StepsAcrossRoute5 = 0 

CountRoute5 = "Yes"

for row in TreeMap:
    if row[StepsAcrossRoute1] == "#":
        TreeCounterRoute1 = TreeCounterRoute1 + 1
    if row[StepsAcrossRoute2] == "#":
        TreeCounterRoute2 = TreeCounterRoute2 + 1
    if row[StepsAcrossRoute3] == "#":
        TreeCounterRoute3 = TreeCounterRoute3 + 1
    if row[StepsAcrossRoute4] == "#":
        TreeCounterRoute4 = TreeCounterRoute4 + 1
    if CountRoute5 == "Yes":
        if row[StepsAcrossRoute5] == "#":
            TreeCounterRoute5 = TreeCounterRoute5 + 1
        StepsAcrossRoute5 = StepsAcrossRoute5 + 1
        CountRoute5 = "No"
    else:
        CountRoute5 = "Yes"
    StepsAcrossRoute1 = StepsAcrossRoute1 + 1
    StepsAcrossRoute2 = StepsAcrossRoute2 + 3
    StepsAcrossRoute3 = StepsAcrossRoute3 + 5
    StepsAcrossRoute4 = StepsAcrossRoute4 + 7
    if StepsAcrossRoute1 > 30:
        StepsAcrossRoute1 = StepsAcrossRoute1 - 31
    if StepsAcrossRoute2 > 30:
        StepsAcrossRoute2 = StepsAcrossRoute2 - 31
    if StepsAcrossRoute3 > 30:
        StepsAcrossRoute3 = StepsAcrossRoute3 - 31
    if StepsAcrossRoute4 > 30:
        StepsAcrossRoute4 = StepsAcrossRoute4 - 31
    if StepsAcrossRoute5 > 30:
        StepsAcrossRoute5 = StepsAcrossRoute5 - 31

print("The answer to part 2 is ", TreeCounterRoute1 * TreeCounterRoute2 * TreeCounterRoute3 * (
    TreeCounterRoute4 * TreeCounterRoute5 ))

