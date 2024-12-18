#lists

grocery_list = ['apple','milk','orange']

data = ['kumar',18,True]

emptylist = []

print('apple' in grocery_list)

print(data[:-1])
print(grocery_list.index('milk'))
print(grocery_list[0:2])
print(grocery_list[-3:-1])

print(len(data))

grocery_list.append("onion")
grocery_list+=['rice']

print(grocery_list)

grocery_list.extend(["fish","chicken"])
print(grocery_list)
print("")
grocery_list.extend(data)
print(grocery_list)
grocery_list.insert(0,"mutton")
print(grocery_list)
grocery_list[2:2] = ["pepper","brinjal"]
print(grocery_list)
grocery_list[1:3]=["chilli",'tomato']
print(grocery_list)

grocery_list.remove(18)

print(grocery_list)

grocery_list.remove(True)

print(grocery_list)

print(grocery_list.pop())

print(grocery_list)

del grocery_list[0]

print(grocery_list)


# del data
#print (data)

print('')
grocery_list[1:2]=["Salt"]
grocery_list.sort()
print(grocery_list)

print('')
grocery_list.sort(key=str.lower)
print(grocery_list)

nums = [3,2,78,1,5]
print(nums)
nums.reverse()
print(nums)
#nums.sort()
nums.sort(reverse=True)
print(nums)
print("")
nums=[1,24,48,3,5]
print(sorted(nums,reverse = True))
print(nums)
print("")

numsCopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]

print(numsCopy)
print(mynums)
mycopy.sort()
print(mycopy)

print('')
print(nums)
print(type(nums))
print('')
mylist=list((1,"kumar",True))
print(mylist)
print('')
#tuple

mytuple = tuple(('Dave',42,True))
anotherTuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))

newList = list(mytuple)
newList.append('Neil')
newtuple = tuple(newList)
print(newtuple)

(one,*two,hey)=anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count(2))