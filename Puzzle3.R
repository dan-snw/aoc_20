# Puzzle 3

library(readr)
library(dplyr)
library(stringr)

Map <- read_csv("inputPuzzle3.txt", col_name = "Markers")

str_length(Map[1,1]) # 31 long before repeating

PointVec <- seq(from = 1, to = 3 * 323, by = 3)

scaleFunction <- function(PointVec) {
  ScaledDown <- ifelse(PointVec > 31, PointVec - 31, PointVec)
  return(ScaledDown)
}

ScaledDown <- PointVec
while (max(ScaledDown) > 31) {
  ScaledDown <- scaleFunction(ScaledDown)
}

Map$Position <- ScaledDown
MapTreed <- Map %>% 
  mutate(Symbol = substr(Markers, ScaledDown, ScaledDown)) %>%
  mutate(Tree = ifelse(Symbol == "#", 1, 0))

sum(MapTreed$Tree)

# 17 mins 45 secs for above

# Part 2

# New Point Vecs
PointVec1 <- seq(from = 1, to = 1 * 323, by = 1)
PointVec2 <- seq(from = 1, to = 3 * 323, by = 3)
PointVec3 <- seq(from = 1, to = 5 * 323, by = 5)
PointVec4 <- seq(from = 1, to = 7 * 323, by = 7)
PointVec5 <- seq(from = 1, to = (0.5 * 323) + 0.5, by = 0.5)

while (max(PointVec1) > 31) {
  PointVec1 <- scaleFunction(PointVec1)
}

while (max(PointVec2) > 31) {
  PointVec2 <- scaleFunction(PointVec2)
}
  
while (max(PointVec3) > 31) {
  PointVec3 <- scaleFunction(PointVec3)
}

while (max(PointVec4) > 31) {
  PointVec4 <- scaleFunction(PointVec4)
}

while (max(PointVec5) > 31) {
  PointVec5 <- scaleFunction(PointVec5)
}

NewMap <- Map %>% 
  mutate(position1 = PointVec1) %>%
  mutate(position2 = PointVec2) %>%
  mutate(position3 = PointVec3) %>%
  mutate(position4 = PointVec4) %>%
  mutate(position5 = PointVec5) %>%
  mutate(position5 = as.character(position5)) %>%
  mutate(position5 = ifelse(grepl(".5", position5), NA, position5)) %>%
  mutate(position5 = as.numeric(position5))

NewMapTreed <- NewMap %>% 
  mutate(Symbol1 = substr(Markers, position1, position1)) %>%
  mutate(Tree1 = ifelse(Symbol1 == "#", 1, 0)) %>%

  mutate(Symbol2 = substr(Markers, position2, position2)) %>%
  mutate(Tree2 = ifelse(Symbol2 == "#", 1, 0)) %>%
  
  mutate(Symbol3 = substr(Markers, position3, position3)) %>%
  mutate(Tree3 = ifelse(Symbol3 == "#", 1, 0)) %>%
  
  mutate(Symbol4 = substr(Markers, position4, position4)) %>%
  mutate(Tree4 = ifelse(Symbol4 == "#", 1, 0)) %>%
  
  mutate(Symbol5 = substr(Markers, position5, position5)) %>%
  mutate(Tree5 = ifelse(Symbol5 == "#", 1, 0)) 

# Down 2 isn't working so try seperately:
SlimmedMap <- Map[seq(1, NROW(Map), by = 2),]
PointVecShort <- seq(from = 1, to = 1 * (324 / 2), by = 1)
while (max(PointVecShort) > 31) {
  PointVecShort <- scaleFunction(PointVecShort)
}
SlimmedMap$position <- PointVecShort
Map5 <- SlimmedMap %>% mutate(Symbol5 = substr(Markers, position, position)) %>%
  mutate(Tree5 = ifelse(Symbol5 == "#", 1, 0)) 
# Get answer
Fin <- NewMapTreed %>% select(contains("Tree")) 
Answer <- sum(Fin$Tree1) * 
  sum(Fin$Tree2) * 
  sum(Fin$Tree3) * 
  sum(Fin$Tree4) * 
  sum(Map5$Tree5)


# Time: 39 mins

