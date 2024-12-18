#Scope

# name="Kumar"

# def greeting(name):
#     age=30
#     print(age)
#     print(name)

# greeting("Subscribe")
# print(name)

# def another():
#     print('')
#     greeting('share')

# another()

name="kumar"
age =18

def another():
    global age
    age+=2
    color = "green"
    def greeting(name):
        nonlocal color #it replaces green to red in memory
        color='red'
        print(color)
        print(name)
        print(age)
    greeting("share")

another()

    