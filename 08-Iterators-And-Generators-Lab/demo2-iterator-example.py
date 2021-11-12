# The iter() function (which calls the __iter__() method) returns an iterator from an iterable

my_list = [4, 7, 0, 3]
# get an iterator using iter()
my_iter = iter(my_list)
print(my_iter) # <list_iterator object at 0x00000000023BC910>
print(next(my_iter))       # 4
print(next(my_iter))       # 7
print(my_iter.__next__())  # 0
print(my_iter.__next__())  # 3
next(my_iter)              # Error
