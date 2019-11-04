class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict_ = {}            

    def get(self, key):

        if key in self.dict_:
            return print(self.dict_[key])
        else:
            return print(-1)

    def set_(self, key, value):
        
        if (len(self.dict_) >= self.capacity):
            keys = []
            values = []
            for key_, value_ in self.dict_.items():
                keys.append(key_)
                values.append(value_)
                
            keys.pop(0)
            values.pop(0)
            
            self.dict_ = {key_:value_ for key_, value_ in zip(keys, values)}

        if (key not in self.dict_):
            self.dict_[key] = value
            
our_cache = LRU_Cache(5)

our_cache.set_(1, 1);
our_cache.set_(2, 2);
our_cache.set_(3, 3);
our_cache.set_(4, 4);

## Test 1: returns 1
our_cache.get(1)

## Test 2: returns 2
our_cache.get(2) 

## Test 3: returns -1
our_cache.get(9)  

# push new element into LRU
our_cache.set_(5, 5) 
our_cache.set_(6, 6)

## Test 4: returns 5
our_cache.get(5) 

## Test 5: returns 6
our_cache.get(6) 

## Test 6: returns -1
our_cache.get(1) 