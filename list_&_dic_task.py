# input 5 girls name using list and take input from users
# input 5 girls ambitions
# input 5  current salaries
# input 5 desired salaries
#check if desired salary is equal to salary

#name1=input('Enter name1 :')
#can also do it like that
#name1=print(input('Enter name1 :')) # takes input and print instantly after input
#name2=input('Enter name2 :')
#name3=input('Enter name3 :')
#name4=input('Enter name4 :')
#name5=input('Enter name5 :')
#print(name1,name2,name3,name4,name5)

#using dictionary inpt names , ambitions, salary and desired salary
name1=input('Enter name1: ')
name2=input('Enter name2: ')
name3=input('Enter name3: ')
name4=input('Enter name4: ')
name5=input('Enter name5: ')

ambition1=input('Enter ambition1: ')
ambition2=input('Enter ambition2: ')
ambition3=input('Enter ambition3: ')
ambition4=input('Enter ambition4: ')
ambition5=input('Enter ambition5: ')

salary1=input('Enter salary1: ')
salary2=input('Enter salary2: ')
salary3=input('Enter salary3: ')
salary4=input('Enter salary4: ')
salary5=input('Enter salary5: ')

desired_salary1=input('Enter desired salary1: ')
desired_salary2=input('Enter desired salary2: ')
desired_salary3=input('Enter desired salary3: ')
desired_salary4=input('Enter desired salary4: ')
desired_salary5=input('Enter desired salary5: ')

dict_1={
    name1:ambition1,
    name2:ambition2,
    name3:ambition3,
    name4:ambition4,
    name5:ambition5
}

dict_2={
    name1:salary1,
    name2:salary2,
    name3:salary3,
    name4:salary4,
    name5:salary5
}

dict_3={
    name1:desired_salary1,
    name2:desired_salary2,
    name3:desired_salary3,
    name4:desired_salary4,
    name5:desired_salary5  }

print(dict_1)
print(dict_2)
print(dict_3)

print("The ", name1 , " has the ambition to become a ", ambition1, " with a current salary of ", salary1, " and a desired salary of ", desired_salary1, salary1==desired_salary1) ,
print("The ", name2 , " has the ambition to become a ", ambition2, " with a current salary of ", salary2, " and a desired salary of ", desired_salary2, salary2==desired_salary2) ,
print("The ", name3 , " has the ambition to become a ", ambition3, " with a current salary of ", salary3, " and a desired salary of ", desired_salary3, salary3==desired_salary3) ,
print("The ", name4 , " has the ambition to become a ", ambition4, " with a current salary of ", salary4, " and a desired salary of ", desired_salary4, salary4==desired_salary4) ,
print("The ", name5 , " has the ambition to become a ", ambition5, " with a current salary of ", salary5, " and a desired salary of ", desired_salary5, salary5==desired_salary5) , 


#using list and dictionary inpt names , ambitions, salary and desired salary



