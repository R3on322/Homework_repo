class Stack:

    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)

    def pop(self):
        return self.data.pop()

    def push(self, elem):
        self.data.append(elem)

    def clear(self):
        self.data = []

    def __repr__(self):  # dunder method
        return ' '.join(self.data)

    def get_data(self):
        return self.data

    def merge_with_other(self, other_stack: 'Stack'):
        empty_stack = []
        if len(self.data) > len(other_stack):
            for index_elem in range(len(other_stack)):
                empty_stack.append(self.data[index_elem])
                empty_stack.append(other_stack[index_elem])
            self.data = empty_stack
        else:
            for index_elem in range(len(self.data)):
                empty_stack.append(self.data[index_elem])
                empty_stack.append(other_stack[index_elem])
            self.data = empty_stack

other_stack = ['6', '7', '1', '6', '7', '8']
stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
stack.push('d')
print(stack)
print(stack.len())
stack.merge_with_other(other_stack)
print(stack)
print(stack.len())
stack.clear()
print(stack)
print(stack.len())