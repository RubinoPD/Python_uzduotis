class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Subject:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = {}  # Saugoti pazymius ir dalyku kreditus

    def add_subject(self, subject, marks):
        """
        Prideti a dalyka su pazymiais studentui.
        """
        self.subjects[subject.name] = {"kreditai": subject.credit, "pazymiai": marks}

    def calculate_average(self):
        """
        Suskaiciuoti ir grazinti vidurki.
        """
        if not self.subjects:
            return 0
        
        total_marks = sum(subject_data["pazymiai"] for subject_data in self.subjects.values())
        return total_marks / len(self.subjects)


subject1 = Subject("Matematika", 3)
subject2 = Subject("Programavimas", 4)

student = Student("Robert Bobert", 29)
student.add_subject(subject1, 7)
student.add_subject(subject2, 9)  

average = student.calculate_average()
print(f"Vidurkis {student.name}: {average}")
