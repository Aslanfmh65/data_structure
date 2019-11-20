## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.string = [None]*26
        self.value = [None]*26
        self.last_char = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        index = ord(char)-ord('a')
        self.string[index] = TrieNode()
        self.value[index] = char
        
    def suffixes(self, suffix=''):
        
        words = []
        
        if (self.last_char is True) and (suffix != ''):
            words.append(suffix)

        for i in range(len(self.string)):
            if self.string[i] is not None:
                char = self.value[i]
                words.extend(self.string[i].suffixes(suffix=suffix+char))
        return words
    
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if node.string[index] is None:
                node.insert(word[i])
            node = node.string[index] 
        node.last_char = True
                

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        if len(prefix) == 0:
            return False
        node = self.root
        print_value = []
        for i in range(len(prefix)):
            index = ord(prefix[i])-ord('a')
            if node.string[index] is None:
                return False
            print_value.append(node.value[index])
            node = node.string[index]
        # print(''.join(print_value))
        return node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)
        

# test 1  
test1 = 'ant'
results = []
pre = MyTrie.find(test1)
results.append(pre.suffixes())
print(results[0] == ['agonist', 'hology', 'onym'])
# Answer: ['agonist', 'hology', 'onym']

# test 2
test2 = 'f'
results = []
pre = MyTrie.find(test2)
results.append(pre.suffixes())
print(results[0] == ['actory', 'un', 'unction'])
# Answer: ['actory', 'un', 'unction']

# test 3
test3 = 'tri'
results = []
pre = MyTrie.find(test3)
results.append(pre.suffixes())
print(results[0] == ['e', 'gger', 'gonometry', 'pod'])
# Answer: ['e', 'gger', 'gonometry', 'pod']

# edge test 1 - the prefix that doesn't exist in stored trie
test3 = 'sw'
pre = MyTrie.find(test3)
print(pre == False)
# Answer: False

# edge test 2 - empty input
test4 = ''
pre = MyTrie.find(test4)
print(pre == False)
# Answer: False