# Keep the class unchanged

class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4

# Extend the base class functionality by adding new class
class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        super().get_discount()
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2


panyo = StudentTaxes('Panyo,', 100, 5.50)

print(panyo.get_discount())

dori = AdditionalDiscount('Dori', 100, 4.50)

print(dori.get_discount())
print(dori.name) # Dori