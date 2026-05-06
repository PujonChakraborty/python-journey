students= ["pujon","risha","arnab","arka"]
print(students)
print(students[1])
print(students[-4])
print(len(students))
for student in students:
    print("welcome,",student,"!")
students.append("Rini")
print(students)    
students.remove("arnab")
print(students)
if "pujon" in students:
    print("pujon is present.")
else:
    print("pujon is missing")
scores = [99,21,27,25,38,53,47,69]
scores.sort()
print(scores)    