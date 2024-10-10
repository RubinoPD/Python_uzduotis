class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Subject:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

class Year:
    def __init__(self, year):
        self.year = year

class ScoreBar:
    def __init__(self, score_ranges):
        """
        Sukuriam balu kartele
        Pvz: { (9, 10): "Labai gerai", (8, 7): "Gerai", (6, 5): "Patenkinamai", (4, 3): "Blogai", (2, 1): "Labai blogai" }
        """
        self.score_ranges = score_ranges

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

    def calculate_subject_average(self, subject_name):
        """
        Paskaiciuojam ir grazinam dalyko vidurki
        """
        if subject_name in self.subjects and self.subjects[subject_name]["marks"]:
            total_marks = sum(self.subjects[subject_name]["marks"])
            return total_marks / len(self.subjects[subject_name]["marks"])
        return 0

    def calculate_overall_average(self):
        """
        Paskaiciuojam ir grazinam bendra vidurki visu dalyku
        """
        total_marks = 0
        total_subjects = 0
        for subject_name, details in self.subjects.items():
            if details["marks"]:
                total_marks += sum(details["marks"]) / len(details["marks"])
                total_subjects += 1
        return total_marks / total_subjects if total_subjects > 0 else 0

    def display_info(self, score_bar=None):
        """
        Atvaizduojam studento informacija
        """
        print(f"Studentas: {self.name}, Amzius: {self.age}")
        for subject_name, details in self.subjects.items():
            average_marks = self.calculate_subject_average(subject_name)
            grade = ""
            if score_bar:
                grade = score_bar.get_grade(average_marks)
            print(f"Dalykas: {subject_name}, Pazymiai: {details["marks"]}, "
                  f"Vidurkis: {average_marks:.2f}, Metai: {details["year"]}, Pazymis: {grade}")



# Sukuriam dalyka
subject1 = Subject("Matematika", 3)
subject2 = Subject("Programavimas", 4)

# Sukuriam metus
year1 = Year(2024)
year2 = Year(2023)

# Sukuriam skale
score_bar = ScoreBar({
    (9, 10): "Labai gerai",
    (7, 8.9): "Gerai",
    (5, 6.9): "Patenkinamai",
    (3, 4.9): "Blogai",
    (1, 2.9): "Labai blogai"
})

# Sukuriam studenta
student = Student("Robert Bobert", 29)
student.add_subject(subject1, year1)
student.add_subject(subject2, year2)

# Pridedam pazymius
student.add_marks("Matematika", [8, 9, 7])  
student.add_marks("Programavimas", [10, 9.5])  

# Atvaizduojam studento informacija
student.display_info(score_bar)

# Atvaizduojam bendra vidurki
overall_average = student.calculate_overall_average()
print(f"Bendras {student.name} vidurkis: {overall_average:.2f}")
