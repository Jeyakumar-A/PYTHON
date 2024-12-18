#Dictionaries
car={
    "brand":"Tesla",
    "model":"Model_3_P",
    "year" : 2024
}
car2=dict(brand="Tesla",model="Model_3")
 
print(car)
print(car2)
print(type(car))
print(len(car))
print("")

#Access items

print(car["brand"])
print(car.get("model"))

#List all keys
print(car.keys())
print(car.values())

#list of key/value pairs as tuples
print(car.items())
#verify a key exists
print("model" in car)
print("price" in car)

#change values
car["brand"]="Nio"
car.update({"price":10000})
print('')
print(car)

#remove items
print(car.pop("price"))
print('')
print (car)

car["ev"]="yes"
print(car)

print(car.popitem)
print('')
print(car)

#delete and clear
car["Ev"] = "yes"
del car["Ev"]
print(car)

car2.clear()
print(car2)
del car2
#Copy dictionaries

# car2=car #create a reference
# print('')
# print(car2)
# print(car)
# car2["Ev"] = "No"
# print(car)

car2=car.copy()
car2["ev"]="no"
print('')
print("good copy")
print(car)
print(car2)

#or use the dict() constructor function
car3 = dict(car)
print('')
print('good copy')
print(car3)

#Nested dictionaries

member1 = {
    "name":"Plant",
    "instrument":"brand"    
}
member2={
    "name":"Page",
    "instrument":"model"
}
band = {
    "member1":member1,
    "member2":member2
}
print('')
print(band)
print(band["member1"]["name"])