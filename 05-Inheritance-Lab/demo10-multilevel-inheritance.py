class Base:
   def __init__(self, name):
      self.name = name

   def get_name(self):
      return self.name

class Child(Base):
   def __init__(self, name, age):
      super().__init__(name)
      self.age = age

   def get_age(self):
      return self.age

class GrandChild(Child):
   def __init__(self, name, age, address):
      super().__init__(name, age)
      self.address = address

   def get_address(self):
      return self.address

grand_child = GrandChild("Grand Name", 19, "Address 15-17")
print(grand_child.name)     # 'Grand Name'
print(grand_child.age)      # '19'
print(grand_child.address)  # 'Address 15-17'


print(GrandChild.__mro__) # (<class '__main__.GrandChild'>, <class '__main__.Child'>, <class '__main__.Base'>, <class 'object'>)