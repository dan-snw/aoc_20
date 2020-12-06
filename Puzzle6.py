# -----------------------------------------------------------------------------
# Puzzle on Day 6
# -----------------------------------------------------------------------------

# Read in input
# -----------------------------------------------------------------------------

CustomForms = open("inputPuzzle6.txt", "r").read().split("\n\n")
CustomForms[-1] = CustomForms[-1][:-1] # hack to take out final new line

# Part 1
# -----------------------------------------------------------------------------

ListOfSets = []
for line in CustomForms:
    LettersByGroup = line.replace("\n", "")
    GroupSet = set(list(LettersByGroup))
    ListOfSets.append(GroupSet)

DeclarationCounter = 0
for EachSet in ListOfSets:
    DeclarationCounter = len(EachSet) + DeclarationCounter

print("Answer to Part 1:", DeclarationCounter)

# Part 2
# -----------------------------------------------------------------------------

JointDeclarationCounter = 0
for line in CustomForms:
    ListOfPeople = line.split("\n")
    SetList = []
    for line in ListOfPeople:
        PersonSet = set(list(line))
        SetList.append(PersonSet)
    IntersectionSet = set.intersection(*SetList)
    JointDeclarationCounter = len(IntersectionSet) + JointDeclarationCounter

print("Answer to Part 2:", JointDeclarationCounter)
