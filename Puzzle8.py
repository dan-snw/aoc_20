# -----------------------------------------------------------------------------
# Puzzle on Day 8
# -----------------------------------------------------------------------------

# Read in Input
# -----------------------------------------------------------------------------
file = open("inputPuzzle8.txt", "r")
steps = file.read().split("\n")

def get_command(command):
    return command[0:3]

def get_sign(command):
    return command[4]

def get_number(command):
    return command[5:]


# Loop through commands until hit cycle repeat 
# -----------------------------------------------------------------------------

# Function for using the commands
def execute_command(linecommand, linenumber, accumulator):
    if get_command(linecommand) == "nop":
        linenumber = linenumber + 1
    if get_command(linecommand) == "acc":
        if get_sign(linecommand) == "+":
            print("boo")
            #accumulator = accumulator + (get_number(linecommand))
            linenumber = linenumber + 1
        else:
            #accumulator = accumulator - (get_number(linecommand))
            print("boo")
            linenumber = linenumber + 1
    if get_command(linecommand) == "jmp":
        linenumber = linenumber + get_number(linecommand)

# Set starting parameters
SetCheck = set()
Looped = False
linenumber = 0
accumulator = 0

# While loop until repeating
while Looped == False:
    if linenumber in SetCheck:
        Looped = True
    else:
        SetCheck.add(linenumber)
        accumulator = accumulator + 4
        execute_command(steps[linenumber], linenumber, accumulator)

print(accumulator)
# Testing the set checker
# -----------------------------------------------------------------------------

#SetCheck = set()
#SetCheck.add(3)
#print(SetCheck)
#print(3 in SetCheck)
#print(4 in SetCheck)
#SetCheck.add(4)
#print(4 in SetCheck)

