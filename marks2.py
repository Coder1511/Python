student_name=input("Enter the student's name: ")
subject_no=[1,2,3]
marks=[]
marks_grade=[]
for subject in subject_no:
   while True:
    mark=int(input(f"Enter the marks of subject {subject}: "))
    if 0<=mark<=100:
      marks.append(mark)
      if 0<=mark<35:
        marks_grade.append("D")
      elif 50>mark>=35:
        marks_grade.append("C")
      elif 75>mark>=50:
        marks_grade.append("B")
      elif 100>=mark>=75:
        marks_grade.append("A")
      break
    else:
        print("Invalid marks entered. Please enter marks between 0 and 100.")   
total_marks=int(sum(marks))
average_marks=total_marks/len(marks)
print("Student Name:",student_name)
print("Total marks:",total_marks)
print("Average marks:",average_marks)
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
for subject in subject_no:
    print(f"Subject {subject} marks: {marks[subject-1]} Grade: {marks_grade[subject-1]}")