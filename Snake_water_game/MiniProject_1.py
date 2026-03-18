import random

def game_win(user,computer):
    if user == computer:
        return None
    # Snake vs water (Snake wins)
    if user == "s" and computer == "w": 
        return True 
    if user == "w" and computer == "s": 
        return False
    
    # Gun vs Snake  (gun wins)
    if user == "g" and computer == "s": 
        return True 
    if user == "s" and computer == "g": 
        return False

    # Water Vs Gun (water wins)
    if user == "w" and computer == "g": 
        return True 
    if user == "g" and computer == "w": 
        return False


rand_no = random.randint(1,3)

print("Computer's turns : Snake(s), Water(w), Gun(g) \n")
if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else: 
    computer = "g"

user = input("Your turn : Snake(s), Water(w), Gun(g) \n").lower()

result = game_win (user,computer) # Returns true if you win, false for loose , None for draw
print(f"\n You choose:{user}")
print(f"\n Computer choose:{computer}")

if result is None:
    print("Its a draw!")
elif (result):
    print("You win!")
else:
    print("You lose!")