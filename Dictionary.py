#Dictionary: Items are ordered,changeable and doesnot allow duplicates
#Key-value

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])

##print the number of items in dictionary

print(len(thisdict))

## dict() method to make dictionary

thisdict = dict(name = "john", age = 29, country = "USA")
print(thisdict)

#get keys method will return a list of all the keys

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x= car.keys()

car["color"]= "white"
print(x)
