# Advent Puzzle 1
library(readr)
library(dplyr)
IN <- read_csv("inputPuzzle1.txt",
         col_names = "List") %>%
  mutate(List = as.factor(List)) 

Expanded <- expand.grid(IN$List, IN$List)

FinalDF <- Expanded %>%
  mutate(Var1 = as.numeric(as.character(Var1))) %>%
  mutate(Var2 = as.numeric(as.character(Var2))) %>%
  mutate(Sum = Var1 + Var2) %>%
  filter(Sum == 2020) %>%
  mutate(Multiplied = Var1 * Var2) 

unique(FinalDF$Multiplied) 

# Part 2

ExpandedBig <- expand.grid(IN$List, IN$List, IN$List)

NextFinalDF <- ExpandedBig %>%
  mutate(Var1 = as.numeric(as.character(Var1))) %>%
  mutate(Var2 = as.numeric(as.character(Var2))) %>%
  mutate(Var3 = as.numeric(as.character(Var3))) %>%
  mutate(Sum = Var1 + Var2 + Var3) %>%
  filter(Sum == 2020) %>%
  mutate(Multiplied = Var1 * Var2 * Var3) 

unique(NextFinalDF$Multiplied) 
NextFinalDF
