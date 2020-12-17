# Puzzle for Day 9 - Cracking the Password
# -----------------------------------------------------------------------------

# Read input
# -----------------------------------------------------------------------------

file = open("inputPuzzle9.txt", "r")
#file = open("TestInput9.txt", "r")
code_raw = file.read().split("\n")
code = []
for line in code_raw:
    if line != "":
        int_line = int(line)
        code.append(int_line)

# Find first sum  
# -----------------------------------------------------------------------------

lower = 0
jump = 25 # set to 5 for testing
still_searching = True
while still_searching == True:
    current_sequence = code[lower:lower + jump]
    product = set()
    for line in current_sequence:
        for lineNext in current_sequence:
            if line != lineNext:
                product.add(int(line) + int(lineNext))
    if int(code[lower + jump]) not in product:
        part_1_answer = code[lower + jump]
        still_searching = False
    else:
        lower = lower + 1
        
print("Answer to Part 1:", part_1_answer)

# Find contiguous weakness
no_answer = True
still_searching_2 = True
while still_searching_2 == True:
    for lower in range(0, len(code)): 
        for upper in range(lower, len(code) + 1):
            total = sum(code[lower:upper])
            if total == part_1_answer and no_answer == True:
                print("Answer to Part 2:" , min(code[lower:upper]) +
                                            max(code[lower:upper]))
                still_searching_2 = False
                no_answer = False
