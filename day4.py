classroom=[]
print ("=== STUDENT GRADE TRACKER ===")
print (" Enter 5 Students and their scores.")
print()

for i in range(1,6):
    name=input("Enter student"+ str(i) + "name:")
    score=int(input("Enter"+name+"'s score:"))
    classroom.append([name,score])

print()
print("=== RESULTS ===")
passed=[]
failed=[]
for student in classroom:
    name=student[0]
    score=student[1]

    if score >=60:
        print(name,"-passed with", score)
        passed.append(name)
    else:
        print(name,"-failed with", score)
        failed.append(name)

print()
print("total students:",len(classroom))
print("passed",len(passed))
print("failed",len(failed))