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
        
    def append(self, new_data):
        if self.tail is None:
            self.tail = Block(time.time(), new_data, previous_hash=None)
            
        else:
            self.tail = Block(time.time(), new_data, self.tail)
            
    def search(self, search_data):
        if self.tail is None:
            print("Block is empty")
            return 
        block = self.tail
        while block:
            if block.data == search_data:
                return block
            block = block.previous_hash
            
        return None

blockchain = Blockchain()

blockchain.append('Income: 40 | Outcome: -20')
blockchain.append('Income: 50 | Outcome: -30')
blockchain.append('Income: 10 | Outcome: -20')
blockchain.append('Income: 80 | Outcome: -40')

## Test 1
print(blockchain.search('Income: 10 | Outcome: -20').data)

## Test 2
print(blockchain.search('Income: 80 | Outcome: -40').data)

## Test 3
print(blockchain.search('Income: 40 | Outcome: -20').data)