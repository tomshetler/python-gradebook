from classroom import ClassRoom
import json

classroom = None

print("Welcome to the gradebook app!")
print("Would you like to start a new class or open an existing one?")
print("A: Open existing class")
print("B: Start a new class")
print("Q: Quit")

choice = input().lower()

if choice == 'a':
    with open('gradebook.json', 'r') as f:
        json_data = json.load(f)
        classroom = ClassRoom.from_json(json_data)
        print("Loaded {} class".format(classroom.name))

if choice == 'b':
    classroom = ClassRoom("Math")

elif choice == 'q':
    print("Goodbye!")

if classroom:
    print("Choose an action: ")
    print("A: See students")
    print("B: Add a student")
    print("C: Get averages")
    print("D: Write classroom to file")
    print("Q: Exit")
    choice = input().lower()

    while choice != 'q':
        classroom.display_menu(choice)
        choice = input().lower()
    print("Goodbye!")