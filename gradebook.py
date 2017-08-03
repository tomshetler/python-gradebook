import classroom

math_class = classroom.ClassRoom("Math")
print("Choose an action: ")
print("A: See students")
print("B: Add a student")
print("C: Get averages")
print("Q: Exit")
choice = input().lower()

while choice != 'q':
    math_class.display_menu(choice)
    choice = input().lower()
print("Goodbye!")