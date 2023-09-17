import random
import time

choice = ["Rock","Paper","Scissors"]
player = ""
while player not in choice:
    player = input("Rock,Paper,Scissor?: ")

enemy = random.choice(choice)
for x in choice:
    print(str(x))
    time.sleep(0.5)

if player == enemy:
    print("Draw! \nThe Enemy also had " + enemy +"!")
elif ((enemy == "Rock" and player == "Scissors") or (enemy == "Paper" and player == "Rock") or (enemy == "Scissors" and player == "Paper")):
    print("You Lost! \nThe Enemy had " + enemy +"!")
else:
    print("You Won! \nThe Enemy had " + enemy +"!")

