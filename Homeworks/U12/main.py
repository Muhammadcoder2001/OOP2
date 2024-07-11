'''Person

Attributes:
name: String
address: String
Methods:
Person(name: String, address: String)
getName(): String
getAddress(): String
setAddress(address: String): void
toString(): String
Student

Attributes:
numCourses: int = 0
courses: String[] = {}
grades: int[] = {}
Methods:
Student(name: String, address: String)
toString(): String
addCourseGrade(course: String, grade: int): void
printGrades(): void
getAverageGrade(): double
toString(): String
Teacher

Attributes:
numCourses: int = 0
courses: String[] = {}
Methods:
Teacher(name: String, address: String)
toString(): String
addCourse(course: String): boolean
removeCourse(course: String): boolean
toString(): String
Notes:

Return false if the course already existed
Return false if the course does not exist
ToString representations:

"Student: name(address)"
"Teacher: name(address)"'''

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_full_info(self)->str:
        return f"""Full info: 
        Name: {self.name} 
        Address: {self.address}"""
    
    def get_name(self)->str:
        return f"Name: {self.name}"
    
    def get_address(self)->str:
        return f"Address: {self.address}"
    
    def set_address(self, new_addres)->str:
        self.address = new_addres

    def toString(self):
        return f""""{self.name}({self.address})" """
    
class Student(Person):
    def __init__(self, name, address, num_course:int):
        super().__init__(name, address)
        self.num_course = num_course
        self.courses:str = []
        self.grades:int = []

    def get_full_info(self) -> str:
        return f"""
        {super().get_full_info()}
        Course Number: {self.num_course}
        Course: {self.courses}
        Grades: {self.grades}"""
    
    def toString(self):
        return f"""
        Student: {super().toString()}"""
        
    def Add_course_grade(self, ncourse:str, ngrade:int)->None:
        self.courses.append(ncourse)
        self.grades.append(ngrade)

    def print_grades(self):

        print(f"Grades: {self.grades}")

    def get_average_grade(self):
        return f"""
        Average: {sum(self.grades)/ len(self.grades)}"""


    def toString(self):
        return f""" Student: 
        Name: "{self.name}({self.address})" """
    
class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.course_int = []
        self.course_str = []

    def add_course(self, course_num:int, course_str:str):
        if course_num not in  self.course_int or course_str not in self.course_str:
            self.course_int.append(course_num)
            self.course_str.append(course_str)
            return True
        else:
            return False
        
    def remove_course(self, rmint:int, rmstr:str):
        if rmint in self.course_int or rmstr in self.course_str:
            self.course_int.remove(rmint)
            self.course_str.remove(rmstr)
            return True
        else:
            return False
        
    def toString(self):
        return f"""Teacher:
        {super().toString()}"""

    def get_full_info(self) -> str:
        return f"""Teacher: 
        {super().get_full_info()}
        Course Number: {self.course_int}
        Course String: {self.course_str}
        """
    
# t1= Teacher("Javohir", "Qashqadaryo")
# p1 = Person("Anvar", "Xorazm")
# s1 = Student("Abror", "Toshkent", 2)
# print(t1.add_course(2, "ikki"))
# print(t1.add_course(3, "Uch"))
# print(t1.remove_course(2, "ikki"))
# print(t1.get_full_info())
# print(t1.toString())

# s1.Add_course_grade("Bir", 1)
# print(s1.get_address())
# print(s1.get_full_info())
# print(s1.Add_course_grade("Ikki", 2))
# print(s1.Add_course_grade("uch", 5))
# print(s1.Add_course_grade("Besh", 3))
# print(s1.Add_course_grade("Olti", 4))
# s1.print_grades()
# print(s1.get_average_grade())
# print(s1.toString())

