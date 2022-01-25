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

    def print_nth_from_last(self, n, method):
        if method ==1:
            total_len = self.len_iterative()

            cur = self.head
            while cur:
                if total_len == n:
                    # print (cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return

        elif method == 2:
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if count >= n:
                        break
                    q = q.next

                if not q:
                    print(str(n) + " is greater than the amount of nodes in list.")
                    return

                while p and q.next:
                    p = p.next
                    q = q.next
                return p.data
            else:
                return None

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome_1(self):
        # Solution 1:
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome_2(self):
        # Solution 2:
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(self):
        # Solution 3
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1
            while count <=i/2 +1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def is_palindrome(self, method):
        if method == 1:
            return self.is_palindrome_1()
        if method == 2:
            return self.is_palindrome_2()
        if method == 3:
            return self.is_palindrome_3()

    def move_tail_to_head(self):
        head = self.head
        tail = self.head
        prev = []

        while tail:
            prev.append(tail)
            tail = tail.next
        tail = prev[-1]
        prev[-2].next = None
        tail.next = head
        self.head = tail

    def sum_two_lists(self, llist):
        ans = LinkedList()
        p = self.head
        q = llist.head
        remainder = 0
        while p and q:
            total = p.data + q.data + remainder
            if total > 9:
                remainder = (total // 10)
                ans.append(total - (remainder * 10))
            else:
                remainder = 0
                ans.append(total)
            p = p.next
            q = q.next

        while p:
            total = p.data + remainder
            if total > 9:
                remainder = (total // 10)
                ans.append(total - (remainder * 10))
            else:
                remainder = 0
                ans.append(total)
            p = p.next

        while q:
            total = q.data + remainder
            if total > 9:
                remainder = (total // 10)
                ans.append(total - (remainder * 10))
            else:
                remainder = 0
                ans.append(total)
            q = q.next
        return ans

# 3 6 5
#   4 2
# ------
#
llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
llist1.sum_two_lists(llist2)