import student


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
        print("Choose an action: ")
        print("A: See students")
        print("B: Add a student")
        print("C: Get averages")
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
