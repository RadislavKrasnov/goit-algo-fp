class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
        cur = cur.next
        return None

    def print_list(self):
        linked_list_str = ""
        current = self.head
        while current:
            linked_list_str += str(current.data) + " "
            current = current.next
        print(linked_list_str)

    def reverseUntil(self, current, previous):
        # last node mark it head
        if current.next is None:
            self.head = current
            #Update next to previous node
            current.next = previous
            return
        
        next = current.next
        current.next = previous
        self.reverseUntil(next, current)
        
    def reverse(self):
        if self.head is None:
            return
        self.reverseUntil(self.head, None)

def merge(head_a, head_b):
    temp = None

    if head_a is None:
        return head_b
    
    if head_b is None:
        return head_a
    
    if head_a.data <= head_b.data:
        temp = head_a
        temp.next = merge(head_a.next, head_b)
    else:
        temp = head_b
        temp.next = merge(head_a, head_b.next)

    return temp

llist_a = LinkedList()
llist_a.insert_at_end(5)
llist_a.insert_at_end(10)
llist_a.insert_at_end(15)
llist_a.insert_at_end(20)
llist_a.insert_at_end(25)

llist_b = LinkedList()
llist_b.insert_at_end(10)
llist_b.insert_at_end(19)
llist_b.insert_at_end(23)
llist_b.insert_at_end(81)
llist_b.insert_at_end(83)

print("Зв'язний список A:")
llist_a.print_list()

print()

print("Зв'язний список B:")
llist_b.print_list()

print()

print("Merged sorted list:")
llist_c = LinkedList()
llist_c.head = merge(llist_a.head, llist_b.head)
llist_c.print_list()
