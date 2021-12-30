class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def delete_node_at_pos(self, pos):
        # Proceed if self.head is not None
        if self.head:
            curr_node = self.head
            # Delete the head node, position 0
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return

            prev = None
            count = 0
            # Travers the linked list until reaching the node in the position or until curr_node is None
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return
            # Delete node
            prev.next = curr_node.next
            curr_node = None

    def len_iterative(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        # key_1 and key_2 represent a means for finding unique nodes to swap
        # if they are equal, they are the same node and nothing to swap
        if key_1 == key_2:
            return

        # Loop through until we find the node that matches key_1 or none match
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # Loop through until we find the node that matches key_2 or none match
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # if no matches for key_1 or key_2 then return
        if not curr_1 or not curr_2:
            return

        # we swap pointers to the second node for the previous node or head
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        # we swap pointers to the first node for the previous node or head
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        # we swap pointers for the current nodes for the next nodes
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dupe_values = dict()

        while cur:
            if cur.data in dupe_values:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before
                dupe_values[cur.data] = 1
                prev = cur
            cur = prev.next

llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()