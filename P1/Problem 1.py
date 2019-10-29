class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict_ = {}            

    def get(self, key):

        if key in self.dict_:
            return print(self.dict_[key])
        else:
            return print(-1)

    def set(self, key, value):

        if (key not in self.dict_):
            self.dict_[key] = value
            
        if (len(self.dict_) > self.capacity):
            self.dict_ = {}
            
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

## Test 1: returns 1
our_cache.get(1)       
## Test 2: returns 2
our_cache.get(2)       
## Test 3: returns -1
our_cache.get(9)      

our_cache.set(5, 5) 
our_cache.set(6, 6)

# Test 4: returns -1
our_cache.get(3) 