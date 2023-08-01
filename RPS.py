import random

choices = ["rock", "paper", "scissors"]

user = input("Please choose rock, paper, scissors: ")

pc = random.choice(choices)

print(f"user: {user}")
print(f"pc: {pc}")

# if user == comp ==> It's a tie!
# u: r c: p ==> you lose!
# u: r c: s ==> you win!
# u: p c: s ==> you lose!
# u: p c: r ==> you win!
# u: s c: p ==> you win!
# u: s c: r ==> you lose!


if pc == user:
    print("its a tie!)")
elif ((user=="paper" and pc=="scissors") or (user=="rock" and pc=="paper") or (user=="scissors" and pc=="rock")):
    print("you lose!")
elif ((user=="rock" and pc=="scissors") or (user=="paper" and pc=="rock") or (user=="scissors" and pc=="paper")):
    print("you win!")
else:
    print("Mistakes were made!")