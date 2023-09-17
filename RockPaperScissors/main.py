import random
import time

player_count = enemy_count = 0

while (True):
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
        enemy_count += 1
    else:
        print("You Won! \nThe Enemy had " + enemy +"!")
        player_count =+ 1
    print("\nEnemy: " +  str(enemy_count) +",Player: " +str(player_count))
    askPlayer = input("Do you wanna player again? y/n: ")
    if (askPlayer != "y"):
        print("Nice game, bye!")
        break
