dog = { "name": "Roger", "age": 9}
print(dog["name"])


dog = { "name": "Roger", "age": 9}
dog["name"] = "Syd"
print(dog)


dog = { "name": "Roger", "age": 9}
print(dog.get("name"))

dog = { "name": "Roger", "age": 9}
print(dog.pop("name"))
print(dog)

print("age" in dog)

dog = { "name": "Roger", "age": 9}
dog["food"] = "Meat"
print(dog)

dog = { "name": "Roger", "age": 9}
del dog["age"]
dog["food"] = "meat"
print(dog)