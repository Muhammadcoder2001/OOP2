'''
4-masala. PROGRAMMER

Developer nomli class yarating va uning property elementlari quyidagilardan iborat:

Surname(Familiyasi);
Position(Lavozimi);
Salary(Oyligi).
SoftwareEngineer nomli class Developer classidan voris bo'lib keladi va uning property elementlari quyidagilardan iborat:

Surname(Familiyasi);
Position(Lavozimi);
Salary(Oyligi);
Bonus(Oylikka qo'shib beriladigan ustama haqi);
Department(Bo'lim nomi).
SoftwareEngineer nomli classning 5ta obyektini yarating. Sizning vazifangiz ushbu obyektlar orasidagi dasturchilarning har bir bo'lim uchun ustama haqi bilan birga qancha summa to'langanligini aniqlang.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmisiz ishlangan misolga past ball qo'yiladi.

Input (Kiruvchi ma'lumot)	Output (Chiquvchi ma'lumot)
Anvar Junior 500 100 1-bo'lim	1-bo'lim 2000
Asror Middle 1500 500 2-bo'lim	2-bo'lim 5300
Kamola Senior 2500 1000 3-bo'lim	3-bo'lim 7800
Vali Junior 500 100 1-bo'lim	
Davron Middle 1500 500 2-bo'lim	
Farrux Junior 500 100 1-bo'lim	
Jamshid Senior 2500 1000 3-bo'lim	
Anvar Junior 500 100 1-bo'lim	
Jasur Senior 2500 1000 3-bo'lim	
Jamila Junior 500 100 1-bo'lim	
'''
class Programmer:
    def __init__(self, surname:str, position:str, salary:int):
        self.surname = surname
        self.position = position
        self.salary = salary
        
class Software_Engineer(Programmer):
    def __init__(self, surname: str, position: str, salary: int, bonus:int, department:str):
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department
        self.summa = 0

engineers = [
    Software_Engineer("Anvar", "Junior", 500, 100, "1-bo'lim"),
    Software_Engineer("Asror", "Middle", 1500, 500, "2-bo'lim"),
    Software_Engineer("Kamola", "Senior", 2500, 1000, "3-bo'lim"),
    Software_Engineer("Vali", "Junior", 500, 100, "1-bo'lim"),
    Software_Engineer("Davron", "Middle", 1500, 500, "2-bo'lim"),
    Software_Engineer("Farrux", "Junior", 500, 100, "1-bo'lim"),
    Software_Engineer("Jamshid", "Senior", 2500, 1000, "3-bo'lim"),
    Software_Engineer("Jasur", "Senior", 2500, 1000, "3-bo'lim"),
    Software_Engineer("Jamila", "Junior", 500, 100, "1-bo'lim"),
]

department_sums = {}
for engineer in engineers:
    total_pay = engineer.salary + engineer.bonus
    if engineer.department in department_sums:
        department_sums[engineer.department] += total_pay
    else:
        department_sums[engineer.department] = total_pay

for department, total_sum in department_sums.items():
    print(f"{department} {total_sum}")








