import random as rd
lottery = input("Enter your lottery number : ")
draw    = rd.randint(1,10000)
if lottery == draw:
  print("You have won the lottery !!!")
else:
  print("Sorry! you missed it. Try it later")