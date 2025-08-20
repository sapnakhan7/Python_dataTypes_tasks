# total = 0
# i=0
# for i in range(2, 51,i+2):  
#     total += i
#     print(f"Step {i}: Sum = {total}")

# take square of evry even i and then sum it like before 

total = 0
for i in range(2, 51, 2):  # even numbers from 2 to 50

    total += i**2
    print(f"Step {i}, Sum = {total}")


    # print("Total sum of squares of even numbers from 2 to 50 is:", total)
