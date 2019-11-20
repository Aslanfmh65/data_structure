## Example Test Case of Ten Integers
import random

def get_min_max(l):
    
    if len(l) == 0:
        return False
    
    small = 100000000000000
    large = 0
    
    for i in l:
        if i <= small:
            small = i
        elif i >= large:
            large = i
 
    return (small,large)

# test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Answer: (0, 9)

# test 2
l = [i for i in range(10, 20)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((10, 19) == get_min_max(l)) else "Fail")
# Answer: (10, 19)

# test 3
l = [i for i in range(20, 40)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((20, 39) == get_min_max(l)) else "Fail")
# Answer: (20, 39)

# edge test 1 - emput input
l = []
random.shuffle(l)
print ("Pass" if (False == get_min_max(l)) else "Fail")
# Answer: False

# edge test 2 - large input
l = [i for i in range(0, 1000000)]
random.shuffle(l)
print ("Pass" if ((0,999999) == get_min_max(l)) else "Fail")
# Answer: (0,999999)