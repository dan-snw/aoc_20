# -----------------------------------------------------------------------------
# Puzzle on Day 7
# -----------------------------------------------------------------------------

# Import
# -----------------------------------------------------------------------------

from collections import defaultdict

# Read in input
# -----------------------------------------------------------------------------

bag_puzzle = open("inputPuzzle7.txt", "r").read().strip().split("\n")
# for testing:
# bag_puzzle = open("TestInput7.txt", "r").read().strip().split("\n")

def string_tidy(string):
    new_string = string.replace(".", "").replace("bags", "bag")
    return new_string

bag_dictionary = {}
for line in bag_puzzle:
    [key,values] = line.split("contain")
    values = values.strip().split(", ")
    values = map(string_tidy, values)
    values = filter(lambda x: x != "no other bag", values)
    values = map(lambda x: tuple(x.split(" ", 1)), values)
    key = string_tidy(key).strip()
    bag_dictionary[key] = list(values)
    
# Reverse the tree for bottom up search
def tree_flip(tree):
    new_tree = defaultdict(list)
    for key,values in tree.items():
        for value,child in values:
            new_tree[child].append(key)
    return(new_tree)

# Define parameters
# -----------------------------------------------------------------------------

flipped_tree = tree_flip(bag_dictionary)
previousLength = -1 
ShinySet = set({"shiny gold bag"})

# Tree search with while loop
# -----------------------------------------------------------------------------
while previousLength != len(ShinySet):
    previousLength = len(ShinySet)
    ThisIterationSet = set()
    for key in ShinySet:
        for colour in flipped_tree[key]:
            ThisIterationSet.add(colour)
    ShinySet = ShinySet.union(ThisIterationSet)

print("Answer to part 1 is", (len(ShinySet) - 1))



