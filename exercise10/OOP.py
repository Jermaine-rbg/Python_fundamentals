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

# what are methods 

class Person():
    def __init__(self,name, age):
        self.name = name
        #self.variable_name is a attribute
        self.age = age
        self.crip = 60

# greeting is a method that takes in no parameter
# and returns a string
    def greeting(self):
        #return f"Hi I\'m {self.name}"
        print(Jermaine.crip)

