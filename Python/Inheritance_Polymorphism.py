class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age >= 18:
            return "He is an adult"
        return "He is a child"

    def is_studying(self):
        print("Humans study from childhood till the age of 18 years as formal education.\n")


class Employee(Human):
    def __init__(self, name, age, company_name, employee_no):
        self.name = name
        self.age = age
        self.company_name = company_name
        self.employee_no = employee_no

    def is_studying(self):
        print("Employees learn on the job.\n")


class Student(Human):
    def __init__(self, name, age, university_name, student_no):
        self.name = name
        self.age = age
        self.university_name = university_name
        self.student_no = student_no

    def is_studying(self):
        print("Students study at the University through lectures.\n")

# class EmployedUndergraduate(Student, Employee):
class EmployedUndergraduate(Employee, Student):
    def __init__(self, name, age, company_name, employee_no, university_name, student_no):
        self.name = name
        self.age = age
        self.company_name = company_name
        self.employee_no = employee_no
        self.university_name = university_name
        self.student_no = student_no

    def is_studying(self):
        print("Student Employees study through lectures and on the job")


if __name__ == '__main__':
    Kasun = EmployedUndergraduate("Kasun", 26, "Cleantech (Pvt) Ltd", 124593, "University of Moratuwa", "170698J")
    print(Kasun.is_adult())
    Kasun.is_studying()