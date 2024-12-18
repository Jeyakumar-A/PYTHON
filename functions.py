#functions

def helloworld():
    print("hello world")


helloworld()

# def sum(num1,num2):
#     return num1+num2

# total=sum(7,44)
# print(total)

# def sum(num1,num2):
#     if(type(num1) is not int or type(num2) is not int):
#         return
#     return num1+num2

# total=sum("kumar",44)
# print(total)

# def sum(num1,num2=8):
#     return num1+num2

# total=sum(7)
# print(total)

# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items("dave","john","sara")

def add(*num):
    sum = 0
    for n in num:
        sum +=n

    print("Sum",sum)
add(9,9,4)


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Subscribe",last="Share")

def func(a,b,*args,option=False,**kwargs):
    print('')
    print(a,b)
    print(args)
    print(option)
    print(kwargs)

func(1,3,10,20,Name='Tom',Salary=6000)