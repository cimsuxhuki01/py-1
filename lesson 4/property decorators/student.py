class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    # Getter method for name property
    @property
    def name(self):
        return self.__name

    # Setter method for name property
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

    #Creating an instance of student

student1 = Student("Amar",17)

print("Name", student1.name)
print("Age", student1.age)

student1.name = "A1ok"
student1.age = 8

print("updated name", student1.name)
print("updated age", student1.age)