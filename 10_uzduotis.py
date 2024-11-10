import random

# Base class for common person details (name, age)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Base class for academic-related details (marks, credits)
class Academic:
    def __init__(self, subject_name, credit):
        self.subject_name = subject_name
        self.credit = credit
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def __str__(self):
        return f"Subject: {self.subject_name}, Credits: {self.credit}, Marks: {self.marks}, Average Score: {self.calculate_average():.2f}"

# Employee class inherits Person
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def __str__(self):
        return f"{super().__str__()}, Position: {self.position}"

# Subject class inherits Academic
class Subject(Academic):
    def __init__(self, subject_name, credit):
        super().__init__(subject_name, credit)


class Year:
    def __init__(self, year):
        self.year = year

    def __str__(self):
        return f"Year: {self.year}"


# Student class inherits both Person and Academic
class Student(Person, Academic):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = []

    def add_subject(self, subject, marks):
        subject.add_marks(marks)
        self.subjects.append((subject, marks))

    def calculate_overall_average(self):
        total_marks = 0
        total_credits = 0

        # Loop through each subject and marks
        for subject, marks in self.subjects:
            subject_avg = sum(marks) / len(marks)  # Calculate average marks for the subject
            total_marks += subject_avg * subject.credit  # Weighted average by credits
            total_credits += subject.credit  # Sum of credits

        # Return the overall average (weighted average)
        return total_marks / total_credits if total_credits else 0

    def assign_specialization(self, average_grade, specialization_criteria):
        for threshold, specialization in specialization_criteria:
            if average_grade >= threshold:
                self.specialization = specialization
                break

    def __str__(self):
        avg_grade = self.calculate_overall_average()
        specialization_info = f", Specialization: {getattr(self, 'specialization', 'None')}"
        subjects_info = "".join([f"\n  Subject: {subject.subject_name}, Marks: {marks}, Average Score: {sum(marks) / len(marks):.1f}" for subject, marks in self.subjects])
        return f"{super().__str__()} {specialization_info}, Overall Average Grade: {avg_grade:.2f}{subjects_info}"

# Function to load data from file
def load_data_from_file(filename):
    students = []
    subjects = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        reading_students = False
        reading_subjects = False

        for line in lines:
            line = line.strip()
            if line == "Students:":
                reading_students = True
                reading_subjects = False
                continue
            elif line == "Subjects:":
                reading_subjects = True
                reading_students = False
                continue

            if reading_students and line:
                name, age = line.split(", ")
                students.append(Student(name.strip(), int(age.strip())))
            elif reading_subjects and line:
                name, credit = line.split(", ")
                subjects.append(Subject(name.strip(), int(credit.strip())))

    return students, subjects

# Main program

employees = [
    Employee("Dalia", 55, "Docente"),
    Employee("Stasia", 45, "Valytoja"),
    Employee("Gabija", 35, "Direktore")
]

# Load data from file
students, subjects = load_data_from_file("students_data.txt")

# Define years and specialization criteria
years = [Year(2023), Year(2024), Year(2025)]
specialization_criteria = [
    (9.0, "Computer Science"),
    (7.5, "Data Science"),
    (6.0, "Software Engineering"),
    (5.0, "Information Technology")
]

# Assign subjects and random marks to each student
for student in students:
    for subject in subjects:
        marks = [random.randint(1, 10) for _ in range(5)]  # Random marks between 1 and 10 for each student
        student.add_subject(subject, marks)

    # Calculate and assign specialization based on the student's average grade
    average_grade = student.calculate_overall_average()
    student.assign_specialization(average_grade, specialization_criteria)


