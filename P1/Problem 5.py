import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
                
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self.calc_hash(data)
        
    def calc_hash(self, string):
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
    
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, new_block=None):
        
        if not new_block:
            print("Can't add block without any data!")
            return
        
        if self.tail is None:
            self.tail = Block(time.time(), new_block, None)
        else:
            new_block = Block(time.time(), new_block, self.tail.hash)
            new_block.previous_block = self.tail
            self.tail = new_block
            
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
                elif block.previous_block:
                    block = block.previous_block
                else:
                    return print("This block cannot be found in blockchain")
        
    def print_block(self):
        if self.tail is None:
            print("Blockchain empty!")
            return 
        block = self.tail
        while block:
            date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp))
            
            print("----------------------------")
            print("Current block: {}".format(block.data))
            print("Storing DateTime: {}".format(date_time))
            print("Block hash value: {}".format(block.hash))
            if block.previous_hash:
                print("Previous hash value: {}".format(block.previous_hash))
                block = block.previous_block
                print("----------------------------")
            
            else:
                return 

# Test 1
# system waits 1s before append next block in order to see the difference in storing date

blockchain = Blockchain()

blockchain.append('Income: 40 | Outcome: -20')
time.sleep(1)
blockchain.append('Income: 50 | Outcome: -30')
time.sleep(1)
blockchain.append('Income: 10 | Outcome: -20')
time.sleep(1)
blockchain.append('Income: 80 | Outcome: -40')

blockchain.print_block()

# Test 2
# system waits 1s before append next block in order to see the difference in storing date

blockchain = Blockchain()

blockchain.append('Income: 1 | Outcome: -1')
time.sleep(1)
blockchain.append('Income: 2 | Outcome: -2')
time.sleep(1)
blockchain.append('Income: 3 | Outcome: -3')
time.sleep(1)
blockchain.append('Income: 4 | Outcome: -4')

blockchain.print_block()

# Edge test 1 - No data input
blockchain = Blockchain()
blockchain.append()

# Edge test 2 - Empty block
blockchain = Blockchain()
blockchain.print_block()

# Edge test 3 - Non existing block
blockchain = Blockchain()
blockchain.append('Income: 40 | Outcome: -20')
blockchain.append('Income: 50 | Outcome: -30')
blockchain.search('Income 100 | Outcome: -100')