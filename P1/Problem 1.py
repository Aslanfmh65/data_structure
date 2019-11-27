class DoubleNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache:
    def __init__(self, capacity):
        self.head = None # most recently used item
        self.tail = None # least recently used item
        self.capacity = capacity
        self.dict_ = {}
        
    def set_(self, new_data = None):
        
        # edge test case
        if new_data is None:
            print("Empty input")
            return
        
        if self.head is None:
            self.dict_[new_data[0]] = DoubleNode(new_data)
            self.head = self.dict_[new_data[0]]
            self.tail = self.head
            return
        elif new_data[0] in self.dict_:
            return print("Pushed element is existing in current LRU")
        
        new_node = DoubleNode(new_data)
        self.dict_[new_data[0]] = new_node
        new_node.next = self.head 
        self.head.previous = new_node 
        self.head = new_node 
        
        if len(self.dict_) > self.capacity:
            node = self.tail
            del self.dict_[node.value[0]]
            node.previous.next = None
            self.tail = node.previous
            node = None
            return
        
    def get(self, call_data):
        if self.head is None or call_data is None:
            return None
        
        node = self.head
                
        if call_data in self.dict_:
            
            # move the call_node from its current position
            call_node = self.dict_[call_data]
            
            if call_node is self.head:
                return call_node.value[1]
                        
            next_node = call_node.next
            previous_node = call_node.previous
            
            if call_node is not self.tail:
                previous_node.next = next_node
                next_node.previous = previous_node
            else:
                previous_node.next = None
                self.tail = previous_node
            
            # move the call_node to the head
            self.head.previous = call_node
            call_node.next = self.head
            self.head = call_node
            
            # return call node value
            return call_node.value[1]
        
        else:
        
            return print("Node does not exist")
    
    def print_node(self):
        if self.head is None:
            return None
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next
        return

## Test 1
# Initial LRU (4,3,2,1)
our_cache = LRU_Cache(5)
our_cache.set_((1,1))
our_cache.set_((2,2))
our_cache.set_((3,3))
our_cache.set_((4,4))

print("Initial LRU:")
our_cache.print_node()

# Call mid-value (3,3), returns (3,3), current LRU key is (3,4,2,1)
get_value = our_cache.get(3)
print("\n\n\nGet mid value is: {}".format(get_value))
print("Current LRU dict:")
our_cache.print_node()

# Call tail-value (1,1), returns (1,1), current LRU key is (1,3,4,2)
get_value = our_cache.get(1)
print("\n\n\nGet tail value is: {}".format(get_value))
print("Current LRU dict:")
our_cache.print_node()

# Call head-value (1,1), returns (1,1), current LRU key is (1,3,4,2)
get_value = our_cache.get(1)
print("\n\n\nGet head value is: {}".format(get_value))
print("Current LRU dict:")
our_cache.print_node()

## Test 2
# push (6,6) and (5,5) into LRU, least recently used item (2,2) disappear
# expect LRU key is (6,5,1,3,4)
print("\n\n\nPush new element into LRU ...")
our_cache.set_((5, 5))
our_cache.set_((6, 6))
print("Current LRU dict:")
our_cache.print_node()

# Call tail-value (4,4), returns (4,4), current LRU key is (4,6,5,1,3,4)
get_value = our_cache.get(4)
print("\n\n\nGet tail value is: {}".format(get_value))
print("Current LRU dict:")
our_cache.print_node()

# Call pushed-out value (2,2), return "node does not exist", current LRU key is (4,6,5,1,3,4)
print("\n\n\n")
get_value = our_cache.get(2)
print("Current LRU dict:")
our_cache.print_node()

## Edge test 1: Empty input
print("\n\n\n")
our_cache.set_()
print("\nCurrent LRU dict:")
our_cache.print_node()

## Edge test 2: String input
print("\n\n\n")
our_cache.set_(('Hello','World'))
get_value = our_cache.get('Hello')
print("\nGet string value is: {}".format(get_value))
print("\nCurrent LRU dict:")
our_cache.print_node()

## Edge test 3: Pushing existing node
print("\n\n\n")
our_cache.set_((6,6))
print("\nCurrent LRU dict:")
our_cache.print_node()