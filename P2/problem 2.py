def rotated_array_search(arr, target):
    
    if len(arr) == 0:
        return -1
    elif type(arr) is not list or type(target) is not int:
        return -1

    pivot_index = find_pivot(arr, 0, len(arr)-1)
    
    if arr[pivot_index] <= target and arr[-1] >= target:
        arr = arr[pivot_index:]
        output = binary_search(arr, 0, len(arr), target)
        return output+pivot_index
        
    elif arr[pivot_index] < target and arr[pivot_index-1] >= target:
        arr = arr[:pivot_index]
        output = binary_search(arr, 0, len(arr), target)
        return output
    
    else:
        return -1

def find_pivot(arr, head, tail):
    
    if head > tail:
        return -1
    elif head == tail:
        return tail
    
    mid = (head+tail)//2
    
    if arr[mid]>arr[mid+1]:
        return mid+1
    elif arr[mid] < arr[mid-1]:
        return mid
    elif arr[head] <= arr[mid]:
        return find_pivot(arr, head, mid-1)
    else:
        return find_pivot(arr, mid+1, tail)
        
def binary_search(arr, head, tail, target):
    mid = (head+tail)//2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binary_search(arr, head, mid, target)
        
    elif arr[mid] < target:
        return binary_search(arr, mid, tail, target)
        
    else:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

#### tests 1-5
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# answer: 0

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# answer: 5

test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# answer: 2

test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# answer: 3

test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# answer: -1

#### edge tests - empty list
test_function([[], -1])
# answer: -1

#### edge tests - not existing target 
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 100])
# answer -1