import os

#r =Read
#a = Append
#w = write
#x = Create

# Read - error if it doesn't exist

f=open("names.txt")
#print(f.read())
#print(f.read(4))

print(f.readline())
print(f.readline())
for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")

finally:
    f.close()

#Append - creates the file if it doesn't exist
f= open("names.txt","a")
f.write("\ncomment")
f.close()

#write(overewrite)

f = open("context.txt","w")
f.write("I deleted all of the context")
f.close()

#Two ways to create a file 
# Opens  a file for writing,create a file if it does not exist
f=open("name_list.txt","w")
f.close()


#creates the specified file,but returns as an error if the file exists

if not os.path.exists("dave.txt"):
    f=open("dave.txt","x")
    f.close()

#delete a file
#avoid an error if it doesn't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")

#with has built-in implicit exception handling

#close() will be automatically called

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)
    