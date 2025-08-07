# using nested if else test courses to decide :
# if module 1 >= 80 percentage 
# (modeule 2 marks ( nested if else)
#  if 90 = cyber , elif 85 = gaming, elif 80 = AI , elif 75 = APP elif 70 = web else ui/graphics)
# elif module 1 >= 60 percentage
# (nested if else 
# if marks >= 70
#print "reappear in test next week "
# else "reappear in test  2 months  ") 
# else print "you cannot appear again for 6 months , until you do complete all necessary courses"



def decide_course(module1_marks, module2_marks):
    if module1_marks >= 80:
        if module2_marks >= 90:
            print ( "Cyber Security" )
        elif module2_marks >= 85:
            print ( "Gaming" )
        elif module2_marks >= 80:
            print ( "Artificial Intelligence" )
        elif module2_marks >= 75:
            print ("App Development" )
        elif module2_marks >= 70:
            print ( "Web Development" )
        else:
            print ( "UI/Graphics Design" )
    elif module1_marks >= 60:
        if module2_marks >= 70:
            print ("Reappear in test next week" )
        else:
            print ( "Reappear in test after 2 months" )
    else:
        print ( "You cannot appear again for 6 months, until you complete all necessary courses" )

print("Enter the marks for Module 1:")
module1 = float(input("Module 1 marks: "))
print("Enter the marks for Module 2:")
module2 = float(input("Module 2 marks: "))

decide_course(module1, module2)
print("Course decision based on your marks has been made.")
# using nested if else to decide course based on module marks

