import random 
# Ask the user for the numbers to be used in the random number generator 
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter a larger number: "))
myNumber = random.randint(smaller,larger)

# Variable to keep track of your number 
count = 0 

# Game mechanics 
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else: 
        print("Congrats!!! You got it in", count, "tries!")
        break