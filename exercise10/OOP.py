jermaine_dict = {
    "name": "Jermaine",
    "age": 44,
}

print(f'jermaine age is: {jermaine_dict["age"]}')

# classses are a way to structure and represent data in custom way 

class Person():
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.crip = 60
        

Jermaine = Person(name="Jermaine", age="44")
print(Jermaine.name)
print(Jermaine.age)
print(Jermaine.crip)
