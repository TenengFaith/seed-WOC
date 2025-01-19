print('''

##### #####  ######   ##    ####  #    # #####  ######    #  ####  #        ##   #    # #####  
  #   #    # #       #  #  #      #    # #    # #         # #      #       #  #  ##   # #    # 
  #   #    # #####  #    #  ####  #    # #    # #####     #  ####  #      #    # # #  # #    # 
  #   #####  #      ######      # #    # #####  #         #      # #      ###### #  # # #    # 
  #   #   #  #      #    # #    # #    # #   #  #         # #    # #      #    # #   ## #    # 
  #   #    # ###### #    #  ####   ####  #    # ######    #  ####  ###### #    # #    # #####  

''')

print("Welcome to the treasure island game")

# You are at a cross road do you to go 'left or right'
direction=input("enter the direction you want to take: ")

# left-> You come to a lake . there is an island in the middle of the lake type 'wait'  to 'wait' to wait for a boat. type 'swim ' to swim across;;;
if direction=="left":
    state=input("you come to an island. Type 'wait' to wait or type 'swim' to swim: ")
    if state=="swim":
        print("you got attacked by an angry truit. game over")
    else:
        print("you arrive at the island unharmed")
        color=input("there is a house with three doors, one yellow, one blue and one red. Which one do you choose:")
        if color=="blue":
            print("game over")
        elif color=="red":
            print("game over")
        elif color=="yellow":
            print("YOU WIN")
else:
    print("game over")
# swim you got attacked by an angry triut. Game over

# wait->you arrived at the island unharmed.there is a house with 3 doors , one yellow and one blue , which color you choose?
# blue-> you entered a room of beast game over
