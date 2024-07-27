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
    
    def sortedInsert(self, head, new_node):
        current = None

        if head == None or head.data >= new_node.data:
            new_node.next = head
            head = new_node
        else:
            current = head
            while current.next != None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        return head

    def insertionSort(self):
        sorted = None
        current = self.head
        while current != None:
            next = current.next
            sorted = self.sortedInsert(sorted, current)
            current = next
        self.head = sorted

llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)
print("Зв'язний список:")
llist.print_list()

print('Insertion Sorted Linked list:')
llist.insertionSort()
llist.print_list()
