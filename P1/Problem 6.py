class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def create_linked_list(self, llist):
        
        if self.head is None:
            self.head = Node(llist[0])
        
        node = self.head
        for index in range(1,len(llist)):
            node.next = Node(llist[index])
            node = node.next
            
    def append(self, new_value):
        if self.head is None:
            self.head = Node(new_value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(new_value)
            
    def search(self, search_node):
        if self.head is None:
            return None
        node = self.head
        while node:
            if node.value == search_node.value:
                return node
            node = node.next
        return None
    
    def printNode(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next

def intersection(llist1, llist2):
    node1 = llist1.head
    intersection_list = LinkedList()
    while node1:
        if llist2.search(node1) and intersection_list.search(node1) is None:
#         if llist2.search(node1):
            intersection_list.append(node1.value)
        node1 = node1.next
    return intersection_list

def union(llist1, llist2):
    union_list = LinkedList()
    node1 = llist1.head
    node2 = llist2.head
    while node1:
        if union_list.search(node1) is None:
            union_list.append(node1.value)
        node1 = node1.next
        
    while node2:
        if union_list.search(node2) is None:
            union_list.append(node2.value)
        node2 = node2.next
    return union_list

## Test 1
llist1 = [3,2,4,35,6,65,6,4,3,21]
llist2 = [6,32,4,9,6,1,11,21,1]

linked_list1 = LinkedList()
linked_list2 = LinkedList()

linked_list1.create_linked_list(llist1)
linked_list2.create_linked_list(llist2)

intersection_list = intersection(linked_list1, linked_list2)
print("Intersection set (unique): ")
intersection_list.printNode()

union_list = union(linked_list1, linked_list2)
print("\nUnion set (unique): ")
union_list.printNode()

## Test 2
llist3 = [3,2,4,35,6,65,6,4,3,23]
llist4 = [1,7,8,9,11,21,1]

linked_list3 = LinkedList()
linked_list4 = LinkedList()

linked_list3.create_linked_list(llist3)
linked_list4.create_linked_list(llist4)

intersection_list = intersection(linked_list3, linked_list4)
print("Intersection set (unique): ")
intersection_list.printNode()

union_list = union(linked_list3, linked_list4)
print("\nUnion set (unique): ")
union_list.printNode()

## Test 3
llist5 = [1,2,3,4,5,4,4,4,4]
llist6 = [4,4,4,4,4,9,9,9,9]

linked_list5 = LinkedList()
linked_list6 = LinkedList()

linked_list5.create_linked_list(llist5)
linked_list6.create_linked_list(llist6)

intersection_list = intersection(linked_list5, linked_list6)
print("Intersection set (unique): ")
intersection_list.printNode()

union_list = union(linked_list5, linked_list6)
print("\nUnion set (unique): ")
union_list.printNode()