from Test.Student import Student


package = __import__("Test")
module = getattr(package,"Student")
student_class = getattr(module, "Student")
student = student_class("00002","frank",42)
student.printStudent()
