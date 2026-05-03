#for i in range(5):
 #   print("you wont recognise me this time")
 #   print("my coding journey:")
#for i in range(1,7):
 #       print ("month",i,"- keep going")
#for i in range(1,6):
#print ("day",i,"- minutes coded so far",i*15)
#i =5 
#while  i > 0 :
 #    print ("coding energy left:",i)
  #   i = i - 1 
#print ("take a break!")
#for i in range (1,100):
 #   print ("checking number",i)
  #  if i== 5:
   #    break 
name = input ("enter your name: ")
total_days=int(input("how many days is your study streak? "))
print ("revewing your study strick MR ",name,"----")
for day in range(1,total_days + 1):
    if day%7== 0:
        print ("day",day,"great! WEEK COMPLETE! dont stop ",name)
    elif day % 3 ==0:
        print("day",day,"not good enough! keep trying")
    else:
        print("day",day,"Showed up. That is all that matters")
 
print("\n---- Streak Complete ----")  

if total_days>=30:
   print("30+ days huh? dont stop now ",name+".")
elif total_days>=21:
   print(" it takes 21 days to make a habbit. congrats MR ",name+"!")
elif total_days>=14:
   print("two week huh . just getting started mr ",name+"!")
else:
   print("day",total_days,".",name+".Every legend started here.")

