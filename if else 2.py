# write python program using if else for absentees using function call parameters  like nested if else for attendance check
# parameters no of leaves
# 5 leaves= 90 %
# 10 leaves 80 %
# 15 leaves 65% with warning
# rest dropout

def check_attendance(no_of_leaves):
    if no_of_leaves <= 5:
        print("Attendance is 90%.")
    elif no_of_leaves <= 10:
        print ("Attendance is 80%.")
    elif no_of_leaves <= 15:
        print ( "Attendance is low, warning issued.")
    else:
        print ("dropped out.")

print("Enter the number of leaves taken by the student:")
no_of_leaves = int(input("Number of leaves: "))
check_attendance(no_of_leaves)
print(check_attendance(no_of_leaves))
