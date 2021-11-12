# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension

print([x ** 2 for x in my_list]) # Output: [1, 9, 36, 100]

# same thing can be done using generator expression

print((x**2 for x in my_list)) # Output: <generator object <genexpr> at 0x0000000002EBDAF8>

a = (x**2 for x in my_list)

print(next(a)) # 1
print(next(a)) # 9
print(next(a)) # 36
print(next(a)) # 100


#print(next(a)) # 100 # StopIteration