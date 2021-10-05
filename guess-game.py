import random

x = random.randint(1,50)
print(x)

for i in range(5):
    bingo = False
    while True:
        try:
            y = int(input("Enter an integer between 1~50: "))
            if x ==y:
                print("You win!")
                bingo = True
                break
            if x>y:
                print("Too low, guess again.")
            else: 
                print("Too high, guess again.")
            break
        except:
            print("Please enter a valid number.")
    if bingo:
        break

if bingo:
    print("Congrats!")
else:
    print(f"Answer is {x}")
    