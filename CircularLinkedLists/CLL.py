class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = self.head
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head


    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head:  # If empty, don't move on
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0

        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        length = len(self)

        if length == 0:
            return None
        if length == 1:
            return self.head

        center = length // 2
        count = 0

        cur = self.head
        prev = None

        while cur and count < center:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        sp_cllist = CircularLinkedList()
        while cur.next != self.head:
            sp_cllist.append(cur.data)
            cur = cur.next
        sp_cllist.append(cur.data)

        self.print_list()
        print("\n")
        sp_cllist.print_list()




# A -> B -> C -> D -> ...
# A -> B -> ... and C -> D -> ...

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

cllist.split_list()
