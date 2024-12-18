#Sets

nums={1,2,3,4}
nums2=set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
#no duplicates allowed
nums={1,2,2,3,4}
print(nums)

#true is a duplicate of 1,false is a duplicate of zero
nums={True,1,2,False,3,4,0}
print(nums)

#check if a value in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#Add anew element to a set
nums.add(8)

#add elements from one set to another set
morenums={5,6,7}
nums.update(morenums)
print(nums)

#you can use update with lists,tuples and dictionaries too

#merge two sets create new set
one={1,2,3}
two={4,5,6}
mynewset=one.union(two)
print(mynewset)

#keep only one duplictes
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

#keep everything except duplicates

one={1,2,3}
two={2,3,4}

one.symmetric_difference_update(two)
print(one)