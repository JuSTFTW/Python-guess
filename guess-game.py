import random

x = random.randint(1,50)
print(x)

for i in range(5):
    y = int(input("Enter an integer between 1~50: "))
    if x ==y:
        print("You win!")
        break
    if x>y:
        print("Too low, guess again.")
    else: 
        print("Too high, guess again.")

print(f"Answer is {x}")
    