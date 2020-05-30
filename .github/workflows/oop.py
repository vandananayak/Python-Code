/*1.the object oriented program mainly focus on
.attributes
.behaviour

2.OOP follow some basic principal
.Inheritance
.encapsulation
.polymorphism*/
#creating class and objecct in python

class Dog:

    # class attribute
    species = "Mammal"

    # instance attribute
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
jim = Parrot("jim", 10)
woo = Parrot("Woo", 5)

# access the class attributes
print("jim is a {}".format(jim.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( jim.name, jim.age))
print("{} is {} years old".format( woo.name, woo.age))
