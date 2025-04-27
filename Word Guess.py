import random

words = ["cat", "mobile"]

choice = random.choice(words)
display = ["_"] * len(choice)

i = 0
while i < 10:
    user = input("Enter the character : ")
    if user in choice:
        for j in range(len(choice)):
            if choice[j] == user:
                display[j] = user
                i += 1
                print(display)
        if "_" not in display:
            print("Congress you win the game...")
            break
    else:
        print("try again")
        i += 1
