class Employee:
    def __init__(self, salary):
        self.__salary = salary

   
    @property
    def salary(self):
        return self.__salary

    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary can't be negative")
        self.__salary = value



emp = Employee(50000)

print("Accessing and updating salary:")


print("emp.salary ->", emp.salary)


emp.salary = 60000
print("emp.salary = 60000 ->", emp.salary)

print("\nTrying a negative value:")


try:
    emp.salary = -300
except ValueError as e:
    print("ValueError:", e)