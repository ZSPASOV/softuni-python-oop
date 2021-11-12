# Create a class Stack which can store only strings and has the following functionality:
# •	Public field: data: list
# •	Public method: push(item)
# •	Public method: pop()
# •	Public method: peek()
# •	Public method: is_empty(): returns boolean
# Override the string method to return the stack data.
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        return self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0


    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'


stack = Stack()
stack.push('baba')
stack.push('dqdo')
print(str(stack))

