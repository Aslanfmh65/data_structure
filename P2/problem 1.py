def sqrt(number):
    if number == None:
        return None
    elif number == 0:
        return 0
    elif number == 1:
        return 1 
    elif type(number) is not int:
        return False
    
    head = number
    half = number // 2
    tail = 0
    
    while True:
        if (head - half) == 1 and (half**2 < number):
            return half
        half = (head - tail)//2 + tail
        if half**2 > number:
            head = half
            continue
        elif half**2 < number:
            tail = half
            half = (head - tail)//2 + tail
            continue
        else:
            return half

#### tests 1-5
print ("Pass" if  (3 == sqrt(9)) else "Fail")
# answer: 3

print ("Pass" if  (0 == sqrt(0)) else "Fail")
# answer: 0

print ("Pass" if  (4 == sqrt(16)) else "Fail")
# answer: 4

print ("Pass" if  (1 == sqrt(1)) else "Fail")
# answer: 1

print ("Pass" if  (5 == sqrt(27)) else "Fail")
# answer: 5

#### tests 6-10
print ("Pass" if  (9 == sqrt(81)) else "Fail")
# answer: 9

print ("Pass" if  (9 == sqrt(90)) else "Fail")
# answer: 9

print ("Pass" if  (31 == sqrt(1000)) else "Fail")
# answer: 31

print ("Pass" if  (2995 == sqrt(8972573)) else "Fail")
# answer: 2995

print ("Pass" if  (35136 == sqrt(1234567890)) else "Fail")
# answer: 35136


#### edge test 1-2
print ("Pass" if  (None == sqrt(None)) else "Fail") # empty test
# answer: None

print ("Pass" if  (False == sqrt("string")) else "Fail") # null/invalid input test
# answer: False