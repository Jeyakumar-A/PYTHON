# def add_one(num):
#     if(num>=9):
#         return num+1
#     total=num+1
#     print(total)
#     return add_one(total)
# mynewtotal= add_one(0)

#program to print factorial of a number recursively

def recursive_factorial(n):
    if n==1:
        return 1
    else:
        return n*recursive_factorial(n-1)

#user input
num=6
#check if the input is valid or not
if num<0:
    print("Invalid input! please enter a positive number")
elif num==0:
    print("factorial of number is 1")
else:
    print("factorial of number  ",num," = ",recursive_factorial(num))