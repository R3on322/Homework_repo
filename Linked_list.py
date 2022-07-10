class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'[{self.val}]->{self.next}'


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)

    def add(self, elem) -> list:
        if not self.head:
            self.head = Node(elem)
            return elem

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(elem)

    def insert(self, elem, index) -> list:
        count = 0
        node = self.head
        prev_node = self.head
        while count != index:
            prev_node = node
            node = node.next
            count += 1
        if count == 0:
            self.add(elem)
        else:
            prev_node.next = Node(elem, next=node)

    def pop(self):
        node = self.head
        prev_node = self.head
        if self.size() != 0:
            if self.size() > 1:
                while node.next:
                    prev_node = node
                    node = node.next
                prev_node.next = None
                return node.val
            else:
                self.head = None
                return node.val
        else:
            return f'List is empty!'

    def remove(self, index) -> list:
        count = 0
        node = self.head
        prev_node = self.head
        while count != index:
            prev_node = node
            node = node.next
            count += 1

        if count == 0:
            self.head = self.head.next

        prev_node.next = node.next

    def clear(self) -> list:
        self.head = None

    def get(self, index):
        count = 0
        node = self.head
        if self.size() >= 1:
            while count != index:
                node = node.next
                count += 1
            return node.val
        else:
            return f'List is empty!'

    def get_first(self):
        if self.size() >= 1:
            return self.head.val
        else:
            return f'List is empty!'

    def get_last(self):
        if self.size() >= 1:
            return self.pop()
        else:
            return f'List is empty!'

    def is_empty(self) -> bool:
        return True if self.size() == 0 else False

    def add_all(self, other_list: 'LinkedList') -> list:
        for elem in other_list:
            self.add(elem)

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def contains(self, elem) -> bool:
        node = self.head

        while node.next:
            if node.val == elem:
                return True
            else:
                node = node.next

        if node.val == elem:
            return True
        else:
            return False

    def to_list(self) -> list:
        node_list = []
        node = self.head
        if self.size() > 1:
            while node.next:
                node_list.append(node.val)
                node = node.next
            node_list.append(node.val)
            return node_list
        else:
            if self.size() == 1:
                node_list.append(node.val)
            return node_list

    def index_of(self, elem) -> int:
        if self.size() != 0 and self.contains(elem):
            count = 0
            node = self.head
            while node.next:
                if node.val == elem:
                    return count
                count += 1
                node = node.next
            return count
        else:
            return f'There is no such element or list is empty!'


other_list = [11, 12, 13, 14, 15]
linked_list = LinkedList()
linked_list.add(100000)
print(linked_list.size())
print(linked_list)
print(linked_list.to_list())