class Linked_list:

    def __init__(self):
        self.data = []

    def __repr__(self):
        return ' '.join(self.data)

    def add(self, elem) -> list:
        self.data.append(elem)


    def insert(self, elem, index) -> list:
        try:
            self.data[index] = elem
        except IndexError:
            print('There is no such index in the list!')

    def pop(self, index=-1):
        return self.data.pop(index)

    def remove(self, index) -> list:
        self.pop(index)

    def clear(self) -> list:
        self.data = []

    def get(self, index):
        return self.data[index]

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(-1)

    def is_empty(self) -> bool:
        return True if self.size() == 0 else False

    def add_all(self, other_list: 'Linked_list') -> list:
        self.data.extend(other_list)

    def size(self) -> int:
        return len(self.data)

    def contains(self, elem) -> bool:
        return True if elem in self.data else False

    # def to_list(self) -> list:
    #     new_data = self.data
    #     return new_data

    def index_of(self, elem) -> int:
        if self.contains(elem) == True:
            return self.data.index(elem)
        else:
            return 'No such item in the list!'


other_list = ['11', '12', '13', '14']
lin_list = Linked_list()
lin_list.add('a')
lin_list.add('1')
lin_list.add('b')
lin_list.add('c')
lin_list.add('2')
lin_list.add('3')
lin_list.add('d')
lin_list.add('e')
lin_list.add('f')
lin_list.add('g')
print(lin_list)
print(lin_list.size())
lin_list.add_all(other_list)
print(lin_list)
print(lin_list.size())