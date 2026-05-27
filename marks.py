marks = []
while True: 
   user_marks = input("Enter your Marks or write done=")
   if user_marks == "done":
    break
marks.append(int(user_marks))
def analyze(marks):
 for m in marks:
   if 100>m>= 33:
    print("The Student has Passed")
   elif 0<m<33:
    print("The Student has Failed")
   else:
    print("Please Input Valid Marks")
print("Highest marks is=",max(marks))
print("Lowest Mraks is=",min(marks))
print("Average Score of Class is=",sum(marks)/len(marks))


   
