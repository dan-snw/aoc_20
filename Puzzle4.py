# -----------------------------------------------------------------------------
# Puzzle on Day 4
# -----------------------------------------------------------------------------

# Full credit to Elliot Greenwood for helpi.... doing this


file = open("inputPuzzle4.txt", "r")
rawInput = file.read()
withDoubleN = rawInput.replace("\n\n", "SplitHerePleaseAndThankyou")
withoutSingleN = withDoubleN.replace("\n", ",")
withoutSpace = withoutSingleN.replace(" ", ",")
splitUp = withoutSpace.split("SplitHerePleaseAndThankyou")

# Pull apart on the colon and commas, then make dictionary

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

splitList = []

for line in splitUp:
    lineRegex = line.replace(":", ",")
    lineList = lineRegex.split(",")
    lineDict = Convert(lineList)
    splitList.append(lineDict)

# Aaaand it's parsed, after just a short 1hr 35 minutes. 
# I'm not gonna time anymore...

# Now for the problem
validCounter = 0
for line in splitList:
    if len(line) == 8:
        validCounter = validCounter + 1
    elif len(line) == 7 and "cid" not in line:
        validCounter = validCounter + 1

print("There are ", validCounter, " valid passwords")

# Problem 2 - adding some conditions

def between(value, lower, upper):
    return value.isnumeric() and lower <= int(value) <= upper

def validate_birth(byr):
    return between(byr, 1920, 2002)

def validate_issue(iyr):
    return between(iyr, 2010, 2020)

def validate_expiry(eyr):
    return between(eyr, 2020, 2030)

def validate_height(hgt, units):
    if units == "cm":
        return between(hgt, 150, 193)
    elif units == "in":
        return between(hgt, 59, 76)
    return False

def validate_eyecolour(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def validate_haircolour(hcl):
    return hcl[0] == "#" and len(hcl) == 7 and hcl[1:].isalnum() 

def validate_pid(pid):
    return pid.isnumeric() and len(pid) == 9

def validate_all(line):
    return (len(line) == 8 or (len(line) == 7 and "cid" not in line)) and \
        validate_birth(line["byr"]) and \
        validate_issue(line["iyr"]) and \
        validate_expiry(line["eyr"]) and \
        validate_height(line["hgt"][:-2], line["hgt"][-2:]) and \
        validate_eyecolour(line["ecl"]) and \
        validate_haircolour(line["hcl"]) and \
        validate_pid(line["pid"]) 

validNumber = len(list(filter(validate_all, splitList)))

print("There are ", validNumber, " valid passwords when extra",
          "restrictions are included")
