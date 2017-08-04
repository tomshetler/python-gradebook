from student import Student
import student
import json


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.student_list = []

    def display_menu(self, option):
        if option == 'a':
            self.get_student_list()
        if option == 'b':
            num_students_to_add = int(input("How many students to add? "))
            for i in range(num_students_to_add):
                self.create_student()
        if option == 'c':
            for student in self.student_list:
                student.get_average_grade(student.grades)
        if option == 'd':
            with open('{}.json'.format(self.name), 'w') as f:
                json.dump(self.json(), f)
                print("Gradebook written to file")

        print("Choose an action: ")
        print("A: See students")
        print("B: Add a student")
        print("C: Get averages")
        print("D: Write classroom to file")
        print("Q: Exit")

    def get_student_list(self):
        if len(self.student_list) < 1:
            print("No students to display.")
        else:
            for student in self.student_list:
                student.get_student_details()

    def create_student(self):
        name = input("Enter student name: ")
        num_classes = int(input("How many classes? "))
        grades = {}
        for x in range(num_classes):
            category = input("Enter category of subject: ")
            category_grades = [int(x) for x in input("Enter students grades: ").split(',')]
            grades.update({category: category_grades})
        new_student = student.Student(name, grades)
        self.student_list.append(new_student)
        return new_student

    def json(self):
        return {
            'name': self.name,
            'student_list': [
                student.json() for student in self.student_list
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        name = json_data["name"]
        student_list = []
        for student_data in json_data["student_list"]:
            student_list.append(Student.from_json(student_data))
        classroom = ClassRoom(name)
        classroom.student_list = student_list
        return classroom
