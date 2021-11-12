from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
        
    @abstractmethod
    def calculate_area(self):
        pass
# TODO: Implement Circle and Rectangle
