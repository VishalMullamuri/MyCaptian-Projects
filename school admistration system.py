class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class SchoolAdministrationSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("List of students:")
            for student in self.students:
                print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")


def main():
    system = SchoolAdministrationSystem()

    while True:
        print("\n*** School Administration System ***")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = int(input("Enter student grade: "))
            system.add_student(name, age, grade)

        elif choice == "2":
            name = input("Enter student name to remove: ")
            system.remove_student(name)

        elif choice == "3":
            system.display_students()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
