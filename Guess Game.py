from random import randint

with open("instructions", mode='r') as f:

    print(f.read())


x = randint(1,100)
count = 0
run = True
y = 0

while run:
    guess = int(input("\n\nEnter your guess between 1 and 100: "))
    if guess == x:
        run = False
        break
    if run and count != 0:
        if abs(guess-x) < abs(y-x):
            print("getting warmer")
        else:
             print("colder")
    if run:
        if abs(guess-x) < 10:
            print("A warm guess: try again")
        else:
            print("cold guess: try again")

    count+=1
    y=guess


if not run:
    print(f"Congratulations you won in just {count}th attempt")




