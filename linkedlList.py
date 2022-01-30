class Node:
    def __init__(self, value=None, next_value=None):
        self.value = value
        self.next_value = next_value


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """ Print the linked list"""
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.value)+"-->"
            itr = itr.next_value

        print(listr)

    def length_list(self):
        """ Return the length of Linked List"""
        if self.head is None:
            print("Length is : 0")
            return

        itr = self.head
        count = 0

        while itr:
            count = count + 1
            itr = itr.next_value
        print("Length is ", count)

    def delete_from_start(self):
        """Delete from the start"""
        self.head = self.head.next_value

    def insert_at_start(self, value):
        """ Insert value at start of Linkedlist"""
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):
        # Blank linkedlist
        if self.head is None:
            node = Node(value, None)
            return
        # Linked List is not blanked
        itr = self.head
        while itr.next_value:
            itr = itr.next_value

        itr.next_value = Node(value, None)

    def insert_list_value(self, values):
        self.head = None
        # print(values)
        for value in values:
            self.insert_at_end(value)

    def find_value(self, target_value):
        itr = self.head
        while itr:
            if itr.value == target_value:
                print("found")
                return
            itr = itr.next_value

        print("Not found")
