# Create a RandomList class that has all the functionality of a List.
# Add additional function that returns and removes a random element from the list.
# •	Public method: get_random_element()
import random

class RandomList(list):
    def get_random_element(self):
        element = random.choice(self)
        self.pop(self.index(element))
        return element


rl = RandomList(['baba', 'dqdo', 'mama'])
print(rl.get_random_element())
print(list(rl))
