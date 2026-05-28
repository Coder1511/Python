student_name=input("Enter the student's name: ")
subject_no=[1,2,3]
marks=[]
for mark in subject_no:
    mark=int(input(f"Enter the marks of subject {subject_no}: "))
    marks.append(mark)
    if mark<35:
        print("The student has a grade D in subject",subject_no)
    elif 50>mark>=35:
        print("The student has a grade C in subject",subject_no) 
    elif 75>mark>=50:
        print("The student has a grade B in subject",subject_no)
    elif 100>=mark>=75:
        print("The student has a grade A in subject",subject_no)
total_marks=sum(marks)
average_marks=total_marks/len(marks)
print("Student Name:",student_name)
print("Total marks:",total_marks)
print("Average marks:",average_marks)
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Grade in subject 1:",marks[0])
print("Grade in subject 2:",marks[1])
print("Grade in subject 3:",marks[2])