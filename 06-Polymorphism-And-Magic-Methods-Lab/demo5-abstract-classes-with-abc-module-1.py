# Abstract-class infrastructure can be implemented using the Abstract Base Classes (ABCs) module
# This module is called abc

# VMESTO :
# class Shape:
#     def __init__(self):
#         if type(self) == Shape:
#             raise TypeError('…')
#     def area(self):
#         raise TypeError('…')
#     def perimeter(self):
#         raise TypeError('…')


# polzvame:

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
