## Creating a dice rolling simulator
## nothing fancy or crazy

##creating the dice
## making a D 2 
d2 <-1:2

##Making dice sets 3 - 20, 50, 100
d3 <- 1:3
d4 <- 1:4
d5 <- 1:5
d6 <- 1:6
d7 <- 1:7
d8 <- 1:8
d9 <- 1:9
d10 <- 1:10
d11 <- 1:11
d12 <- 1:12
d13 <- 1:13
d14 <- 1:14
d15 <- 1:15
d16 <- 1:16
d17 <- 1:17
d18 <- 1:18
d19 <- 1:19
d20 <- 1:20
d50 <- 1:50
d100 <- 1:100

##making the roll funtions
## to "roll the dice simply input roll#(fates = dice sides you want ) 
## example roll1(fates = d15)

## making a 1 dice roll
roll1<- function(fates){
dice <- sample(fates, size = 1, replace = TRUE)
sum(dice)
}

## Making 2 - 10 dice rolls, you might not roll more than one d100, but you might roll 10 d4's

roll2<- function(fates){
dice <- sample(fates, size = 2, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll3<- function(fates){
dice <- sample(fates, size = 3, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll4<- function(fates){
dice <- sample(fates, size = 4, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll5<- function(fates){
dice <- sample(fates, size = 5, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll6<- function(fates){
dice <- sample(fates, size = 6, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll7<- function(fates){
dice <- sample(fates, size = 7, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll8<- function(fates){
dice <- sample(fates, size = 8, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll9<- function(fates){
dice <- sample(fates, size = 9, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}

roll10<- function(fates){
dice <- sample(fates, size = 10, replace = TRUE)
print ("Dice Values")
print(dice)
print("Sum of Dice")
sum(dice)
}




