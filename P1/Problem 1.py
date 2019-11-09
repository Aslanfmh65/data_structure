class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict_ = {}
        
    def set_(self, key, value):
        if key is None or value is None:
            print("Empty input")
            return
        elif type(key) != int or type(value) != int:
            return print("Invalid input")
        
        new_dict = {}
        new_dict[key] = value
        count = 0
        for i in self.dict_:
            count += 1
            if count >= self.capacity:
                break
            new_dict[i] = self.dict_[i]
        self.dict_ = new_dict

    def get(self, key):
        if key in self.dict_:
            value = self.dict_[key]
            del self.dict_[key]
            self.set_(key, value)
            return self.dict_[key]
        else:
            return -1
        
    def print_dict(self):
        for i in self.dict_:
            print(i, end=' ')

print("\n")
print("Initial LRU (4,3,2,1)")
our_cache = LRU_Cache(5)
our_cache.set_(1,1)
our_cache.set_(2,2)
our_cache.set_(3,3)
our_cache.set_(4,4)
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Test 1: call 1, returns 1, LRU (1,4,3,2)")
value = our_cache.get(1)
print("Get value is: {}".format(value))
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Test 2: call 2, returns 2, LRU (2,1,4,3)")
value = our_cache.get(2) 
print("Get value is: {}".format(value))
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Test 3: call 9, returns -1, LRU (2,1,4,3)")
value = our_cache.get(9)  
print("Get value is: {}".format(value))
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Push new element into LRU, LRU (6,5,2,1,4)")
our_cache.set_(5, 5) 
our_cache.set_(6, 6)
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Test 4: call 5, returns 5, LRU (5,6,2,1,4)")
value = our_cache.get(5) 
print("Get value is: {}".format(value))
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Test 5: call 6, returns 6, LRU (6,5,2,1,4)")
value = our_cache.get(6)
print("Get value is: {}".format(value))
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Test 6: call 3, returns -1, LRU (6,5,2,1,4)")
value = our_cache.get(3)
print("Get value is: {}".format(value))
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Edge test 1: empty input")
value = our_cache.set_(None, None)
print("Current LRU dict:")
our_cache.print_dict()

print("\n")
print("Edge test 2: invalid input")
value = our_cache.set_('Hello', 'World')
print("Current LRU dict:")
our_cache.print_dict()