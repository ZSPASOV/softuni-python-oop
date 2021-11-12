from abc import ABC, abstractmethod


class StudentTaxes(ABC):
    def __init__(self, name, semester_fee, average_grade):
        self.name = name
        self.semester_fee = semester_fee
        self.average_grade = average_grade

    @abstractmethod
    def get_discount(self):
        pass


class ExcellentStudent(StudentTaxes):
    def get_discount(self):
        return self.semester_fee * 0.4


class AverageStudent(StudentTaxes):
    def get_discount(self):
        return self.semester_fee * 0.3


# ako se poqvqvat if else v nashite methods tova e indikaciq che nai veroqtno narushavame open/closed principa
# prezapisvaneto na metoda se smqta za extension a ne za modification