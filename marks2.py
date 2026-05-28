student_name=input("Enter the student's name: ")
subject_no=[1,2,3]
marks=[]
marks_grade=[]
for subject in subject_no:
    mark=int(input(f"Enter the marks of subject {subject}: "))
    marks.append(mark)
    if mark<35:
        marks_grade.append("D")
    elif 50>mark>=35:
        marks_grade.append("C")
    elif 75>mark>=50:
        marks_grade.append("B")
    elif 100>=mark>=75:
        marks_grade.append("A")    
total_marks=sum(marks)
average_marks=total_marks/len(marks)
print("Student Name:",student_name)
print("Total marks:",total_marks)
print("Average marks:",average_marks)
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Grade in subject 1:",marks_grade[0])
print("Grade in subject 2:",marks_grade[1])
print("Grade in subject 3:",marks_grade[2])