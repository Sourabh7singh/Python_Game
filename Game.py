import random
user_win=0
computer_win=0

options=["rock","paper","scissor"]

while True:
       user_input=input("Type rock/paper/scissor or q to quit or s to view score? ").lower()
       if user_input=="q":
              break
       if(user_input=="s"):
              print(f"you win {user_win} times")
              print(f"computer win {computer_win} times")
       if (user_input not in ["rock","paper","scissor"]):
              continue
       random_number=random.randint(0,2)
       computer_pick=options[random_number]
       print(f"computer picked {computer_pick}") 
       if(user_input=="rock" and computer_pick=="scissor"):
              print("You won! ")
              user_win+=1
              continue
       if(user_input=="paper" and computer_pick=="rock"):
              print("You won! ")
              user_win+=1
              continue
       if(user_input=="scissor" and computer_pick=="paper"):
              print("You won! ")
              user_win+=1
              continue            
       if (user_input=="scissor" and computer_pick=="scissor"):
              print(f"You both pick {user_input}")
              continue
       if (user_input=="rock" and computer_pick=="rock"):
              print(f"You both pick {user_input}")
              continue
       if (user_input=="paper" and computer_pick=="paper"):
              print(f"You both pick {user_input}")
              continue
       else:
              print("you loose! ")
              computer_win+=1
              continue    
