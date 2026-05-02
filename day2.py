#name=input("whats your name? ")
#age= input("how old are you? ")
#city=input ("where do you live? ")
#print ("--------------------")
#print (" nice to meet you,",name)
#print ("you are ", age, "years old",name)
#print ("you are from", city, name)
#print("-------------------------")
#ages = 17 
#if ages >= 18:
 #   print ("You can apply for scholarship!")
#elif ages>= 15:
 #   print("you need a guardian to apply.")
#else:
 #   print("sorry, you are too young ")
name = input ("Enter your name: ")
age = input ("enter you age: ")
age = int(age)
print ("---------------------------------")
if age >= 20:
    print ( "Congratulations Mr. ",name + "!")
    print ("you are eligible to apply for scholarship. time to hustle")
elif age>=15:
    print("almost there MR. ", name + "!")
    print ("you are", 18-age, "years away from eligibility.")
else:
    print ("Hey MR. ", name)
    print ("you are too young MR.",name,".Wait till your time and grind your skill till then.")
    print("---------------------------------------------")
    print ("program complete!")