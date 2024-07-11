class Employee:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

    def get_info(self) -> str:
        return f"""
        Surname: {self.surname} 
        Position: {self.position}  
        Salary:{self.salary}$"""
    

class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary, rating):
        super().__init__(surname, position, salary)

        self.rating = rating

    def get_info(self):
        return f"""{super().get_info()}
        Rating: {self.rating}"""
    
lst = [
Enterprise_employee("Smith", "Manager", 75000, 65),
Enterprise_employee("Johnson", "Developer", 90000, 77),
Enterprise_employee("Williams", "Designer", 65000, 83),
Enterprise_employee("Brown", "Analyst", 70000, 96),
Enterprise_employee("Jones", "Tester", 60000, 94)
]

for employee in lst:
    if employee.rating < 75:
        employee.salary *= 1.2
        print(employee.get_info())
    elif employee.rating < 90:
        employee.salary *= 1.4
        print(employee.get_info())

    elif employee.rating > 89:
        employee.salary *= 1.6
        print(employee.get_info())





