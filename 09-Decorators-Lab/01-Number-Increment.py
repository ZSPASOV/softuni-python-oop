def number_increment(numbers):
    def increase():
        return [n + 1 for n in numbers] # ne slagame nonlocal zashtoto samo chetem numbers, ne go mutirame
    return increase()


print(number_increment([1, 2, 3]))


# principno stava i:
# def number_increment(numbers):
#    return [n + 1 for n in numbers]
