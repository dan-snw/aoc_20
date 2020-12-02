# Puzzle on 2 December
library(readr)
library(dplyr)

Input <- read_delim("inputPuzzle2.txt", 
                    delim = c(":"),
                    col_names = c("Condition", "Password"))

library(stringr)
library(tidyr)
TidyInput <- Input %>%
  mutate(Password = str_replace(Password, " ", "")) %>%
  #mutate(LowerBound = str_split_fixed(Condition, "-", 1))
  separate(Condition, c("Bounds", "Letter"), " ") %>%
  separate(Bounds, c("LowerBound", "UpperBound"), "-") %>%
  mutate(LowerBound = as.numeric(LowerBound)) %>%
  mutate(UpperBound = as.numeric(UpperBound)) 

Tested <- TidyInput %>% mutate(OccurenceCount = str_count(Password, Letter)) %>%
  mutate(WithinBoundary = case_when(
    OccurenceCount >= LowerBound & OccurenceCount <= UpperBound ~ 1,
    TRUE ~ 0))
sum(Tested$WithinBoundary)

# Part 2
Tested2 <- TidyInput %>% 
  mutate(FirstLetter = substr(Password, LowerBound, LowerBound)) %>%
  mutate(SecondLetter = substr(Password, UpperBound, UpperBound)) %>%
  mutate(ValidPassword = case_when(
    FirstLetter == SecondLetter ~ 0, 
    FirstLetter != Letter & SecondLetter != Letter ~ 0, 
    TRUE ~ 1))

sum(Tested2$ValidPassword)
Tested2 <- TidyInput

