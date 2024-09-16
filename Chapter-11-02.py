class Student:
    # class attributes
    school = 'Dandelion Academi'
    course = 'Python'
    count = 0
    # init funcion is the constructor of the class
    def __init__(self, f_name, l_name, gender, age):
        Student.count += 1
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

    def print_fullname(self):
        print(f'{self.f_name.title()} {self.l_name.title()}')

    def year_born(self):
        return 2024 - self.age

std1 = Student('Navid', 'Arian', 'M', 32)    
std1.school = "Manely's School"
std1.count = Student.count
std2 = Student('Yaser', 'Ghaderipour', 'M', 34)
std2.count = Student.count
print(std1.school)
print(std2.school)
print('All students number:', Student.count) 
print('Student No1:', std1.count)
print('Student No2:', std2.count)
print(std1.f_name, std1.l_name, std1.gender, std1.age)
print(std2.f_name, std2.l_name, std2.gender, std2.age)

std1.print_fullname()
print(std1.year_born())

std2.print_fullname()
print(std2.year_born())