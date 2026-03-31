from abc import ABC , abstractmethod
#
# height in meters , weight in kg
#
# collect_user_data()
#
# print_results()
#
# print_info()
#
# run()
#
# get_bmi_category() abstract method to categories bmi into underweight normal weight overweight obese on age specific thresholds
#
# calculate_bmi() abstract method to calculate bmi based on specific formulas for adults and children
#
# formula BMI = weightkg/heightkg
# categories for adult class
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 24.9
# Overweight: 24.9 <= BMI < 29.9
# Obese: BMI >= 29.9

# categories for child class
# Underweight: BMI < 14
# Normal weight: 14 <= BMI < 18
# Overweight: 18 <= BMI < 24
# Obese: BMI >= 24
# formula Adjusted BMI = weightkg/heightkg

class BMI(ABC):
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def category(self):
        pass


class Adult(BMI):
    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2) + 1e-6, 1)

    def category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal"
        elif bmi < 29.9:
            return "Overweight"
        return "Obese"


class Child(BMI):
    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2) + 1e-6, 1)

    def category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal"
        elif bmi < 24:
            return "Overweight"
        return "Obese"


age = int(input("Age: "))
height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

person = Adult(age, height, weight) if age >= 18 else Child(age, height, weight)

bmi = person.calculate_bmi()
print("BMI:", round(bmi, 1))
print("Category:", person.category())
