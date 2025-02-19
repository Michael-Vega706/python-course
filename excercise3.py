class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def present(self):
        return f"My name is {self.name}, I'm {self.age} years old."
    
person1 = Person("John Doe", 25)
print(person1, type(person1))

class Student(Person):
    
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def __str__(self):
        return f"{super().__str__()} I'm in grade {self.grade}."
    
    
    def present(self):
        return f"{super().present()} My grade is {self.grade}."

# person1 = Student("John Doe", 25)
# print(person1, type(person1))
student1 = Student("Jane Doe", 20, 5)
print(student1, type(student1))
print(student1.present())
print(person1.present())