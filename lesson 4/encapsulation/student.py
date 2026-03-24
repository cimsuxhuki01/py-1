class Student:
    def __init__(self, name , age):
        #initialize Private Attribute
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

student1 = Student("Amar",16)
print("Name", student1.get_name())
student1.set_name("Ok")
print("updated name", student1.get_name())
student1.set_age(1)
print("updated age", student1.get_age())