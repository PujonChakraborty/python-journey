classroom=[]
print("enter the name of the students:")
print("enter their scores :")
print()
for i in range(1,6):
    name=input("Enter student"+ str(i)+"name:")
    score=int(input("enter"+name+"'s score:"))
    classroom.append([name,score])
print()
print(" RESULT ")
passed=[]
failed=[]
scores=[]
for student in classroom:
    name =student[0]
    score=student[1]

    if score>=60:
        print(name,"-passed with",score)
        passed.append(name)
    else:
        print(name,"failed with",score)
        failed.append(name)

print("Total Students:",len(classroom))
for student in classroom:
    scores.append(student[1])
print("Highest score :",max(scores))
print( "lowest :",min(scores))
print("Average of the class:",sum(scores)/len(scores))
classroom.sort(key=lambda s: s[1],reverse=True)
print()
print("=== LEADERBOARD ===")
position=1
for student in classroom:
    print(position,".",student[0],"-",student[1])
    position=position+1
#scholarship
print()
top_student=classroom[0]
if top_student[1]>=93:
    print("Scholarship awarded to:", top_student[0],"scored",top_student[1],"-outstanding!")
elif top_student[1]>=85:
    print(top_student[0],"scored",top_student[1],"-close ! push harder !")
else:
    print("not enough try harder ! top scorer was",top_student[0],"with",top_student[1])


