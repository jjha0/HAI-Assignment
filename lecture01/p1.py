class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
    
    def display_info(self):
        print("ID:", self.student_id, "/ 이름:", self.name, "/ 나이:", self.age)

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def display_all_students(self):
        for student in self.students:
            student.display_info()

student1 = Student("1번", "김철수", "20살")
student2 = Student("2번", "이영희", "21살")
student3 = Student("3번", "박지민", "19살")

manager = StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("현재 등록된 학생 목록:")
manager.display_all_students()

student4 = Student("4번", "한지수","22살")
manager.add_student(student4)

print("\n학번 4번 학생 추가 후:")
manager.display_all_students()
