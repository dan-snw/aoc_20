# -----------------------------------------------------------------------------
# Puzzle for Day 5
# -----------------------------------------------------------------------------

# Read in
# -----------------------------------------------------------------------------
file = open("inputPuzzle5.txt", "r")
BoardingPassList = file.read().split("\n")[0:-1]

# Create Functions
# -----------------------------------------------------------------------------

def make_binary_pass(BoardingPass):
    return BoardingPass.replace("F", "0").replace("B", "1").replace(
           "L","0").replace("R", "1")

def find_only_row(BoardingPass):
    return make_binary_pass(BoardingPass)[0:7]

def find_only_seat(BoardingPass):
    return make_binary_pass(BoardingPass)[7:]

def get_num(BinaryNum):
    return int(BinaryNum, 2)

def get_seat_id(BoardingPass):
    return (8 * get_num(find_only_row(BoardingPass)) + 
            get_num(find_only_seat(BoardingPass)))

# Testing that the conversions work
# -----------------------------------------------------------------------------

#BFFFBBFRRR: row 70, column 7, seat ID 567.
print("Test 1 - should be 567. It's", get_seat_id("BFFFBBFRRR"))
#FFFBBBFRRR: row 14, column 7, seat ID 119.
print("Test 2 - should be 119. It's", get_seat_id("FFFBBBFRRR"))
#BBFFBBFRLL: row 102, column 4, seat ID 820.
print("Test 3 - should be 820. It's", get_seat_id("BBFFBBFRLL"))

# Part 1 - Find Maximum Seat ID
# -----------------------------------------------------------------------------

# Convert all boarding passes
SeatIDList = []
for line in BoardingPassList:
    SeatIDList.append(get_seat_id(line))
OrderedSeats = sorted(SeatIDList)

print("The highest seat ID is", OrderedSeats[-1])

# Part 2 - Find my missing middle seat
# -----------------------------------------------------------------------------

# Find max
i = OrderedSeats[0]
while i < OrderedSeats[-1]:
    i = i + 1
    if i not in OrderedSeats:
        MySeat = i

print("My seat is", MySeat)
