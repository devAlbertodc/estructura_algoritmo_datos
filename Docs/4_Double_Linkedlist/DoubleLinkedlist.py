from Node import Node


class DoubleLinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or self.length <= index:
            return None

        temp = self.head
        if index < self.length / 2:
            # Si el índice está más cerca del inicio, miramos desde head hacia tail:
            for _ in range(index):
                temp = temp.next
        else:
            # Si el índice está más cerca del final, miramos desde tail hacia head:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or self.length < index:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        # Nodos anteriores y posteriores para redirigir los punteros:
        before = self.get(index - 1)
        after = before.next
        # Reasignacion de los punteros del nuevo nodo hacia los nodos anterior y posterior:
        new_node.prev = before
        new_node.next = after
        # Reasignacion de los punteros existentes al nuevo nodo:
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or self.length <= index:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        before = self.get(index-1)
        delete = before.next
        after = delete.next

        before.next = after
        after.prev = before

        delete.prev = None
        delete.next = None
        self.length -= 1
        return delete


