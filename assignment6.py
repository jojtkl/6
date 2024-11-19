# Build a program to manage a university's course catalog. You want to define a base class Course that has the following properties:
# course_code: a string representing the course code (e.g., "CS101")
# course_name: a string representing the course name (e.g., "Introduction to Computer Science")
# credit_hours: an integer representing the credit hours for the course (e.g., 3)
# You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
# CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major.
# ElectiveCourse should have an additional property elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").


class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_course_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credit Hours: {self.credit_hours}")

# Subclass for CoreCourse
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        Course.__init__(self, course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_course_info(self):
        Course.display_course_info(self)
        print(f"Required for Major: {'Yes' if self.required_for_major else 'No'}")

# Subclass for ElectiveCourse
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        Course.__init__(self, course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_course_info(self):
        Course.display_course_info(self)
        print(f"Elective Type: {self.elective_type}")

# Example usage
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
print("Core Course Information:")
core_course.display_course_info()

print("\n")

elective_course = ElectiveCourse("HUM201", "Introduction to Philosophy", 3, "liberal arts")
print("Elective Course Information:")
elective_course.display_course_info()
print("\n")
print('Q2_________________________________________________________________________________________________')#



#Create a Python module named employee that contains a class Employee with attributes name, salary and
# methods get_name() and get_salary().
# Write a program to use this module to create an object of the Employee class and display its name and salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

# Create an Employee object
emp = Employee("Jerin", 5000000)

# Display the employee's name and salary
print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())



#------------------------------------------------------------------------------------------------------------------------#
# class Course:
#     def __init__(self,course_code,course_name,credit_hours):
#         self.course_code=course_code
#         self.course_name=course_name
#         self.credit_hours=credit_hours
#
#     def display_course_info(self):
#         print(f"Course Code: {self.course_code}")
#         print(f"Course Name: {self.course_name}")
#         print(f"Credit Hours: {self.credit_hours}")
#
# # Subclass for CoreCourse, inheriting from Course
# class CoreCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, required_for_major):
#         self.course_code=course_code
#         self.course_name=course_name
#         self.credit_hours=credit_hours
#         self.required_for_major = required_for_major
#
#     def display_course_info(self):
#         Course.display_course_info(self)
#         print(f"Required for Major: {'Yes' if self.required_for_major else 'No'}")
#
# class ElectiveCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, elective_type):
#         self.course_code=course_code
#         self.course_name=course_name
#         self.credit_hours=credit_hours
#         self.elective_type = elective_type
#
#     def display_course_info(self):
#         Course.display_course_info(self)
#         print(f"Elective Type: {self.elective_type}")
#
#
# core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
# #print("Core Course Information:")
# core_course.display_course_info()
#
# print("\n")
#
#
# elective_course = ElectiveCourse("HUM201", "Introduction to Philosophy", 3, "liberal arts")
# #print("Elective Course Information:")
# elective_course.display_course_info()
