import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        
    def calc_hash(self, string):
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
    
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.tail = None
        
    def append(self, new_block):
        if self.tail is None:
            self.tail = Block(time.time(), new_block, None)
        else:
            self.tail = Block(time.time(), new_block, self.tail)
            
    def search(self, find_block):
        if find_block is None:
            print("Empty input")
            return
        elif type(find_block) != str:
            print("Invalid input")
            return
        
        if self.tail is None:
            return None
        else:
            block = self.tail
            while block:
                if block.data == find_block:
                    return block.data
                else:
                    block = block.previous_hash
            
            print("This block cannot be found in blockchain")
            return

blockchain = Blockchain()

blockchain.append('Income: 40 | Outcome: -20')
blockchain.append('Income: 50 | Outcome: -30')
blockchain.append('Income: 10 | Outcome: -20')
blockchain.append('Income: 80 | Outcome: -40')

print("\n")
print("Test 1")
print(blockchain.search('Income: 10 | Outcome: -20'))

print("\n")
print("Test 2")
print(blockchain.search('Income: 80 | Outcome: -40'))

print("\n")
print("Test 3")
print(blockchain.search('Income: 40 | Outcome: -20'))

print("\n")
print("Test 4")
print(blockchain.search('Income 100 | Outcome: -100'))

print("\n")
print("Edge test 1: empty input")
blockchain.search(None)

print("\n")
print("Edge test 2: invalid input")
blockchain.search(1234)