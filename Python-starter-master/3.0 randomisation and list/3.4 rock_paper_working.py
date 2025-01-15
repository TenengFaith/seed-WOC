#ascii.co.uk/art
import random
user_option=input("enter your desired option;either rock, paper or scissors: ")
if user_option=="rock":
    user=1
    print("""
          
      ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"

    """)
elif user_option=="paper":
    user=2
    print("""
          
        ___..__
__..--- '._ __.'
              "-..__
            '"--..__";
___        '--...__"";
    `-..__ '"---..._;"
          '''----'     
         
           """)
elif user_option=="scissors":
    user=3
    print("""
          
   ____
  / __ \
( (__) |___ ___
  \________,'   '''''----....____
   _______<  () dd       ____----'
 / __   __`.___-----''''
( (__) |
  \____/

          """)
number=random.randint(1,3)
print("THe computer chooses:")
if number==1:
    print("""
      ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
          """)
elif number==2:
        print("""
           ___..__
  __..--''' ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          ''''----'     
          """)
elif number==3:
         print("""
   ____
  / __ \
 ( (__) |___ ___
  \________,'   '''''----....____
   _______<  () dd       ____----'
  / __   __`.___-----''''
 ( (__) |
  \____/

          """)
if user==number:
      print("it is a tie")
elif user==1 and number==3:
      print("rock crushes scissors. You win")
elif number==1 and user==3:
      print("rock crushes scissors, You loose")
elif user==2 and number==1:
      print("paper covers rock, You win")
elif number==2 and user==1:
      print("paper covers rock, You loose")
elif user==3 and number==2:
      print("scissors cuts paper, You win")
elif number==3 and user==2:
      print("scissors cuts paper, You loose")

