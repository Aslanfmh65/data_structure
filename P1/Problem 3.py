import sys
from collections import deque

# Linked list
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Define queue data structure
class Queue():
    def __init__(self):
        self.d = deque()
        
    def enq(self, value):
        self.d.append(value)

    def deq(self):
        if len(self.d) > 0:
            pop_value = self.d.popleft()
            return pop_value
        else:
            return None
        
    def get_len(self):
        return len(self.d)

# Binary tree

class Tree:
    def __init__(self):
        self.q = []
        
        self.binary_dict = {}
        self.queue = Queue()
        self.queue_equal = Queue()
        self.queue_unequal = Queue()
        
    def frequency(self, input_string):
        keys = list(set([i for i in input_string]))
        values = [0] * len(keys)
        
        for i in input_string:
            values[keys.index(i)] += 1
            
        char_freq = {k:v for k,v in zip(keys,values)}
        char_freq = sorted(char_freq.items(), key=lambda x:x[1])
        
        return char_freq
    
    def push_to_queue(self, char_freq):
        for item in char_freq:
            node = Node(item[0], item[1])
            self.queue.enq(node)
            
    def merge_to_root(self):
        while (self.queue.get_len() > 1):
            node1 = self.queue.deq()
            node2 = self.queue.deq()
            freq = node1.freq + node2.freq
            root_node = Node(None, freq)
            root_node.left = node1
            root_node.right = node2
            self.queue.enq(root_node)
            
    def assign_binary(self, root, binary_code):
        if root is None:
            return
        
        if root.char is not None:
            self.binary_dict[root.char] = binary_code
            return
        
        # recursion 
        self.assign_binary(root.left, binary_code + "0")
        self.assign_binary(root.right, binary_code + "1")
        
    def traverse(self):
        root = self.queue.deq()
        binary_code = ""
        self.assign_binary(root, binary_code)

def encoding(input_string):
    
    tree = Tree()
    # sort a string into tuple based on frequency
    char_freq = tree.frequency(input_string)

    # push each tuple into queue data structure
    tree.push_to_queue(char_freq)

    # merge two nodes into one root and push into queue 
    tree.merge_to_root()

    # assign binary code to left and right child of root
    tree.traverse()

    # show the dictionary after Huffman coding
    dict_ = tree.binary_dict
    
    encoded_text = [dict_[i] for i in input_string]
    encoded_text = '-'.join(encoded_text)
    
    return encoded_text, dict_

def decoding(encoded_text, dict_):
    
    if type(input_string) != str:
        print("Error: Invalid input")
        return [-1,-1]
    
    elif input_string is None or len(input_string) == 0:
        print("Error: Empty input")
        return [-1,-1]
    
    code = [i for i in encoded_text.split('-')]
    dict_ = {v:k for k,v in dict_.items()}
    text = [dict_[j] for j in code]
    return ''.join(text)

def huffman(input_string):
    
    if type(input_string) != str:
        print("Invalid input")
        return [-1,-1]
    
    elif input_string is None or len(input_string) == 0:
        print("Empty input")
        return [-1,-1]
    
    elif len(set(input_string)) == 1:
        return '0'*len(input_string) + '/'+'1'*len(input_string)
    

    [encoded_text, dict_] = encoding(input_string)
    decoded_text = decoding(encoded_text, dict_)
    
    input_size = sys.getsizeof(input_string)
    encoded_text = ''.join(encoded_text.split('-'))
    encoded_size = sys.getsizeof(int(encoded_text, base=2))
    decoded_size = sys.getsizeof(decoded_text)
    
    return [input_size, encoded_text, encoded_size, decoded_size, decoded_text]

## Test 1
print("\n")
input_string = "The bird is a word"
[input_size, encoded_text, encoded_size, decoded_size, decoded_text] = huffman(input_string)
print("The size of the data is: {}".format(input_size))
print("The content of the data is: {}".format(input_string))
print("The size of the encoded data is: {}".format(encoded_size))
print("The content of the encoded data is: {}".format(encoded_text))
print("The size of the decoded data is: {}".format(decoded_size))
print("The content of the encoded data is: {}".format(decoded_text))

## Test 2
print("\n")
input_string = "Udacity is great"
[input_size, encoded_text, encoded_size, decoded_size, decoded_text] = huffman(input_string)
print("The size of the data is: {}".format(input_size))
print("The content of the data is: {}".format(input_string))
print("The size of the encoded data is: {}".format(encoded_size))
print("The content of the encoded data is: {}".format(encoded_text))
print("The size of the decoded data is: {}".format(decoded_size))
print("The content of the encoded data is: {}".format(decoded_text))

## Test 3
print("\n")
input_string = "Huffman code is a famous algorithm"
[input_size, encoded_text, encoded_size, decoded_size, decoded_text] = huffman(input_string)
print("The size of the data is: {}".format(input_size))
print("The content of the data is: {}".format(input_string))
print("The size of the encoded data is: {}".format(encoded_size))
print("The content of the encoded data is: {}".format(encoded_text))
print("The size of the decoded data is: {}".format(decoded_size))
print("The content of the encoded data is: {}".format(decoded_text))

## Edge Test 1: Empty input
print("\n")
input_string = ''
huffman(input_string)

## Edge Test 2: Invalid input
print("\n")
input_string = 123456789
huffman(input_string)

## Edge Test 3: Repeated string input
print("\n")
input_string = 'aaaaa'
print(huffman(input_string))