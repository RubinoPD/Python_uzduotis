import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Subject:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Subject: {self.name}, Credits: {self.credit}"


class Year:
    def __init__(self, year):
        self.year = year

    def __str__(self):
        return f"Year: {self.year}"


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = {}
        self.specialization = None

    def add_subject(self, subject, year, marks):
        self.subjects[subject.name] = {
            "credit": subject.credit,
            "marks": marks,
            "year": year.year
        }

    def calculate_overall_average(self):
        total_marks = 0
        total_count = 0
        for subject, details in self.subjects.items():
            marks = details["marks"]
            total_marks += sum(marks)
            total_count += len(marks)
        return total_marks / total_count if total_count > 0 else None

    def assign_specialization(self, average_grade, specialization_criteria):
        for threshold, specialization in specialization_criteria:
            if average_grade >= threshold:
                self.specialization = specialization
                break

    def __str__(self):
        student_info = f"Student: {self.name}, Age: {self.age}, Specialization: {self.specialization}"
        subjects_info = ""
        for subject, details in self.subjects.items():
            avg_score = sum(details["marks"]) / len(details["marks"]) if details["marks"] else "N/A"
            subjects_info += f"\n  Subject: {subject}, Credits: {details['credit']}, Marks: {details['marks']}, Average Score: {avg_score}"
        return student_info + subjects_info


# Function to read student and subject data from a file
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


# Function to save students' results to a file
def save_results_to_file(filename, students):
    with open(filename, 'w') as file:
        for student in students:
            file.write(str(student) + "\n")
            file.write("-" * 50 + "\n")


# Load data from input file
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
    for subject, year in zip(subjects, years):
        marks = [random.randint(1, 10) for _ in range(5)]
        student.add_subject(subject, year, marks)

    # Calculate and assign specialization based on the student's average grade
    average_grade = student.calculate_overall_average()
    student.assign_specialization(average_grade, specialization_criteria)

# Save results to output file
save_results_to_file("student_results.txt", students)

# Print to console
for student in students:
    print(student)
    print("\n" + "-" * 50 + "\n")
