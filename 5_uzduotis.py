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


class ScoreBar:
    def __init__(self, score_ranges):
        """
        Sukuriam balu kartele
        { (9, 10): "Labai gerai", (8, 7): "Gerai", (6, 5): "Patenkinamai", (4, 3): "Blogai", (2, 1): "Labai blogai" }
        """
        self.score_ranges = score_ranges

    def __str__(self):
        ranges_str = ', '.join([f"{k[0]}-{k[1]}: {v}" for k, v in self.score_ranges.items()])
        return f"Score Bar: {ranges_str}"

    def get_grade(self, score):
        """
        Paimti pazymi atspindinti balu kartele
        """
        for score_range, grade in self.score_ranges.items():
            if score_range[0] <= score <= score_range[1]:
                return grade
        return "No grade"


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = {}  # Dictionary laikyti mokymosi dalykus, pazymius ir metus
        self.specialization = None  # Specializacijos bus priskirtos atitinkamai nuo vidurkio

    def add_subject(self, subject, year, marks):
        """
        Prideti dalyka ir akademinius metus studentui
        """
        self.subjects[subject.name] = {
            "credit": subject.credit,
            "marks": marks,
            "year": year.year
        }

    def calculate_overall_average(self):
        """
        Paskaiciuoti visu dalyku vidurki
        """
        total_marks = 0
        total_count = 0
        for subject, details in self.subjects.items():
            marks = details["marks"]
            total_marks += sum(marks)
            total_count += len(marks)
        return total_marks / total_count if total_count > 0 else None

    def assign_specialization(self, average_grade, specialization_criteria):
        """
        Priskiria specializacija priklausomai nuo vidurkio
        """
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


# Create several subjects
subjects = [
    Subject("Matematika", 3),
    Subject("Python programavimas", 4),
    Subject("AI veido atpazinimas", 3)
]

# Define years for each subject
years = [
    Year(2023),
    Year(2024),
    Year(2025)
]

# Create several students
students = [
    Student("Robertas", 29),
    Student("Domantas", 31),
    Student("Rimante", 30)
]

# Define specialization criteria based on average grade thresholds
specialization_criteria = [
    (9.0, "Computer Science"),
    (7.5, "Data Science"),
    (6.0, "Software Engineering"),
    (5.0, "Information Technology")
]

# Assign subjects and random marks to each student
for student in students:
    for subject, year in zip(subjects, years):
        # Random marks between 1 and 10 for the subject
        marks = [random.randint(1, 10) for _ in range(5)]
        student.add_subject(subject, year, marks)

    # Calculate and assign specialization based on the student's average grade
    average_grade = round(student.calculate_overall_average(), 1)
    student.assign_specialization(average_grade, specialization_criteria)

# Print each student's information including their specialization
for student in students:
    print(student)
    print("\n" + "-" * 50 + "\n")
