student = {}

for i in range(5):
    student_name = input("Enter name: ")
    student_score = int(input("Enter score: "))
    student[student_name] = student_score

print(student)
print(student.get('gagan'))

for i,j in student.items():
    print (i,j)
    total=totali+j
    avg=total/len(student)