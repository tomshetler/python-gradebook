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

    def json(self):
        return {
            'name': self.name,
            'grades': self.grades
        }

    @classmethod
    def from_json(cls, json_data):
        return Student(json_data["name"], json_data["grades"])