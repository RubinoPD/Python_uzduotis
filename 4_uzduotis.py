
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
        Pvz: { (9, 10): "Labai gerai", (8, 7): "Gerai", (6, 5): "Patenkinamai", (4, 3): "Blogai", (2, 1): "Labai blogai" }
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
        return "No grade"  # Grazina default value jeigu nerandama pazymio


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = {}  # Dictionary laikyti mokymosi dalykus, pazymius ir metus

    def add_subject(self, subject, year):
        """
        Prideti dalyka ir akademinius metus studentui
        """
        self.subjects[subject.name] = {
            "credit": subject.credit,
            "marks": [],
            "year": year.year
        }

    def add_marks(self, subject_name, new_marks):
        """
        Prideti pazymius
        """
        if subject_name in self.subjects:
            self.subjects[subject_name]["marks"].extend(new_marks)
        else:
            print(f"Dalykas {subject_name} nerastas!")

    def calculate_average(self, subject_name):
        """
        Paskaiciuoti pazymiu vidurki
        """
        if subject_name in self.subjects:
            marks = self.subjects[subject_name]["marks"]
            if marks:
                return sum(marks) / len(marks)
        return None

    def __str__(self):
        student_info = f"Student: {self.name}, Age: {self.age}"
        subjects_info = ""
        for subject, details in self.subjects.items():
            avg_score = self.calculate_average(subject)
            subjects_info += f"\n  Subject: {subject}, Credits: {details['credit']}, Average Score: {avg_score if avg_score is not None else 'N/A'}"
        return student_info + subjects_info


# Function to print choices and select from them

def print_choices(choices):
    """
    Print the available choices and let the user select them
    """
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")
    selected = int(input("Select an option by number: ")) - 1
    if 0 <= selected < len(choices):
        return choices[selected]
    else:
        print("Invalid choice. Try again!")
        return None


# Create several subjects

subjects = [
    Subject("Matematika", 3),
    Subject("Python programavimas", 4),
    Subject("AI veido atpazinimas", 3)
]

# Create several years
years = [
    Year(2023),
    Year(2024),
    Year(2025)
]

# Create a score bar
score_bars = [
    ScoreBar({
        (9, 10): "Labai gerai",
        (7, 8.9): "Gerai",
        (5, 6.9): "Patenkinamai",
        (3, 4.9): "Blogai",
        (1, 2.9): "Labai blogai"
    })
]

# Create several students
students = [
    Student("Robertas", 29),
    Student("Domantas", 31),
    Student("Rimante", 30)
]

# Select a student
print("Select a student:")
selected_student = print_choices(students)
if selected_student:
    print(f"Selected student: {selected_student}\n")

# Select a subject
print("Select a subject:")
selected_subject = print_choices(subjects)
if selected_subject:
    print(f"Selected subject: {selected_subject}\n")

# Select a year
print("Select a year:")
selected_year = print_choices(years)
if selected_year:
    print(f"Selected year: {selected_year}\n")

# Select a score bar
print("Select a score bar:")
selected_score_bar = print_choices(score_bars)
if selected_score_bar:
    print(f"Selected score bar: {selected_score_bar}\n")

# Add selected subject and year to the student
if selected_student and selected_subject and selected_year:
    selected_student.add_subject(selected_subject, selected_year)
    print(f"Added {selected_subject.name} to {selected_student.name} for the year {selected_year.year}.")

# Input marks for each subject
if selected_student and selected_subject:
    marks = []
    print(f"Enter marks for {selected_subject.name} (type 'done' to finish):")
    while True:
        mark = input("Enter mark:")
        if mark.lower() == 'done':
            break
        try:
            marks.append(float(mark))
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")

    # Add marks to the subject for the selected student
    selected_student.add_marks(selected_subject.name, marks)

    # Calculate and display the average and grade
    avg_score = round(selected_student.calculate_average(selected_subject.name), 1)
    grade = selected_score_bar.get_grade(avg_score) if avg_score is not None else "N/A"
    print(f"Average Score for {selected_subject.name}: {avg_score}")
    print(f"Grade: {grade}")

    print("\nStudent's updated info:")
    print(selected_student)