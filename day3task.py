import random
name = input("enter your name: ")
secret = random.randint(1, 10)

tries = 0
print ("im thinking of a number from 1-10")
print ("can you guess?")
print ("-------------------------------------")
while True:
      guess=input("guess the number: ")
      guess=int(guess)
      tries=tries+1
      if guess==secret:
        print("wow great!",name+" its matched!")
        break 
      elif guess>secret:
       print("too big",name)
      else:
       print("too small")

print ("-------------")
print(" the number was ",secret)
print("number of tries tooK: ",tries)       