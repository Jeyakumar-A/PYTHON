#loops
#while loop
# i=1
# while i <10 :
#     i+=1
#     if i==3:
#         continue
#     print(i)
# else:
#     print("i is no longer less than 10")

#For loop

# fruits = ["apple","banana","mango"]
# for x in fruits:
#     if x=="banana":
#         continue
#     print(x)

# for x in "share":
#     print(x)

# for x in range(10):
#     print (x)

# for x in range(2,4):
#     print(x)

for x in range(0,101,5):
    print(x)
else:
    print("glad thats over")

names=["Balachandra","dave","Ganesh"]
actions=["codes","eats","sleeps"]

for name in names:
    for action in actions:
        print(name+" "+action+".")
for action in actions:
    for name in names:
        print(action+" "+name+".")