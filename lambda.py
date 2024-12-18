#lambda
squared = lambda num: num*num
print(squared(3))

add_two = lambda num:num+2
print(add_two(4))

sum_total = lambda a,b:a+b
print(sum_total(5,5))

def functionBuilder(x):
    return lambda num: num+x

add_ten = functionBuilder(10)
add_twenty = functionBuilder(20)

print(add_ten(7))
print(add_twenty(7))

numbers=[3,7,12,18,20,21]

squared_nums = map(lambda num:num*num,numbers)
print(list(squared_nums))

odd_nums = filter(lambda num:num%2 !=0,numbers)
print(list(odd_nums))

from functools import reduce

numbers =[1,2,3,4,5,1]

total = reduce(lambda acc,curr:acc+curr,numbers)

print(total)

print(sum(numbers))

names=['kumar','dave gray','suresh']

char_count = reduce(lambda acc,curr:acc+len(curr),names,0)
print(char_count)