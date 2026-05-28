marks = []

while True:
    user_marks = input("Enter your marks or type done: ")
    if user_marks.lower() == "done":
        break
    if not user_marks.isdigit():
        print("Please enter a valid numeric mark or 'done'.")
        continue
    marks.append(int(user_marks))
def analyze(marks):
    for m in marks:
        if 0 <= m < 33:
            print(f"{m}: The student has failed")
        elif 33 <= m <= 100:
            print(f"{m}: The student has passed")
        else:
            print(f"{m}: Please input valid marks")


if marks:
    analyze(marks)
    print("Highest marks is=", max(marks))
    print("Lowest marks is=", min(marks))
    print("Average score of class is=", sum(marks) / len(marks))
else:
    print("No marks were entered.")


   
