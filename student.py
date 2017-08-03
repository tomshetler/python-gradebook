class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average_grade(self, grades):
        for category in grades:
            average = sum(grades[category]) / len(grades[category])
            print("{} scored a {} in {}".format(self.name, average, category))

    def get_student_details(self):
        print(self.name)
        print(self.grades)