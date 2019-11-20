def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    
    if len(input_list) == 0:
        return [-1]
    
    sorted_list =  mergesort(input_list)
    
    digit1 = ''
    digit2 = ''
            
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            digit1 += str(sorted_list[i])
        else:
            digit2 += str(sorted_list[i])
    return [int(digit1), int(digit2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#### tests 1-3
test_function([[1, 2, 3, 4, 5], [531, 42]])
# Answer: [531, 42]

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Answer: [964, 852]

test_function([[0, 6, 9, 3, 7, 8, 1], [9730, 861]])
# Answer: [9730, 861]

#### edge tests - empty list
test_function([[], [-1]])
# Answer: [-1]

#### edge tests - large number
test_function([[0, 4, 8, 9, 1, 2, 6, 3, 7, 5], [97531, 86420]])
# Answer: [97531, 86420]