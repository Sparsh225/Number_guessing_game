from art import logo
print(logo)
import random
from replit import clear
def check(chance):
  state=True
  while chance!=0:
    num=int(input("Make a guess:"))
    if(num>guess):
      chance=chance-1
      print("To high !")
      print(f"you have {chance} attempts remainig to guess the number")
    elif(num<guess):
      chance=chance-1
      print("To low !")
      print(f"you have {chance} attempts remainig to guess the number")
    else:
      chance=chance-1
      state=False
      print(f"you have {chance} attempts remainig to guess the number")
      print("you guessed the right number , You won")
  clear()    
  print("You Loose, you dont have any attempts left ")
      
print("Welcome to a number guessing game !")
print("Im thinking of anumber between 1 and 100")
guess=random.randint(1,100)
level=input("DO YOU WANT TO PLAY THE HARD LEVEL OR LOW LEVEL ? TYPE 'h' or 'l' ").lower()
if(level=='h'):
  chance=5
  print("You have 5 attempts remainig to guess the number")
  check(chance)
else:
  print("You have 10 attempts remaining to guess the number ")
  chance=10
  check(chance)
