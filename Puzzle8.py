<<<<<<< HEAD
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
=======
# Puzzle for Day 9 - Cracking the Password
# -----------------------------------------------------------------------------

# Read input
# -----------------------------------------------------------------------------

#file = open("inputPuzzle8.txt", "r")
file = open("TestInput8.txt", "r")
steps = file.read().split("\n")

#test = steps[1].split(" ")[0]

# Functions for executing steps
# -----------------------------------------------------------------------------

def jump(counter, number):
    if number[0] == "-":
        counter = counter - int(number[1:])
    if number[0] == "+":
        counter = counter + int(number[1:])
    return counter

def accumulate(accumulator, counter, number):
    if number[0] == "-":
        accumulator = accumulator - int(number[1:])
    if number[0] == "+":
        accumulator = accumulator + int(number[1:])
    counter = counter + 1
    return accumulator, counter

def noop(counter):
    counter = counter + 1
    return counter

def call_right_function(command, counter, accumulator):
    command_broken = command.split(" ")
    instruction = command_broken[0]
    number = command_broken[1]

    if instruction == "acc":
        accumulator,counter = accumulate(accumulator, counter, number)
    
    if instruction == "jmp":
        counter = jump(counter, number)

    if instruction == "nop":
        counter = noop(counter)
    
    return counter,accumulator

# Part 1
# -----------------------------------------------------------------------------

counter = 0
accumulator = 0

already_executed = set()
infinite_loop_found = False
while infinite_loop_found == False:
    latest_command = steps[counter]
    counter,accumulator = \
        call_right_function(latest_command, counter, accumulator)
    if counter in already_executed:
        print("Answer to part 1:", accumulator)
        infinite_loop_found = True
    else:
        already_executed.add(counter)

# Part 2
# -----------------------------------------------------------------------------

# Wildly inefficient but just want to hack it at this point
counter = 0 
accumulator = 0
change_found = False
current_changer = 0

while change_found == False and current_changer < len(steps):
    print(current_changer)
    already_executed = set()
    infinite_loop_found = False
    while infinite_loop_found == False and counter < len(steps):
        latest_command = steps[counter]
        if counter == current_changer:
            if latest_command[0:3] == "jmp":
                new_latest_command = "nop" + latest_command[3:]
            elif latest_command[0:3] == "nop":
                new_latest_command = "jmp" + latest_command[3:]
        else: 
            new_latest_command == latest_command
   
        if new_latest_command == "":
            change_found = True
            print("Answer to Part 2:", accumulator)
            print("Found by changing the value of line", current_changer)
            break
        counter,accumulator = \
            call_right_function(new_latest_command, counter, accumulator)
        if counter in already_executed:
            counter = 0
            accumulator = 0
            infinite_loop_found = True
        else:
            already_executed.add(counter)
    current_changer = current_changer + 1


# Testabadooping
# -----------------------------------------------------------------------------

#counter = 0
#accumulator = 0

#already_executed = set()
#infinite_loop_found = False
#print(steps[8])
#steps[8] = steps[8].replace(steps[8][0:3], "nop")
#print(steps[8])
#while infinite_loop_found == False:
    #latest_command = steps[counter]
    #counter,accumulator = \
        #call_right_function(latest_command, counter, accumulator)
    #if counter in already_executed:
        #print("Answer to part 3:", accumulator)
        #infinite_loop_found = True
    #else:
        #already_executed.add(counter)
>>>>>>> 259754c52bcfd809b495673491e37dfec5df95b4

