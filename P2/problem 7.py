# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, input_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        
        for item in path:
            if item not in node.children:
                node.insert(item)
            node = node.children[item]
        node.last_char = True
        node.handler = input_handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for item in path:
            if item not in node.children:
                return None
            node = node.children[item]
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None
        self.last_char = False

    def insert(self, char):
        # Insert the node as before
        self.children[char] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        splited_path = self.split_path(path)
        self.route_trie.insert(splited_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        if path is "/":
            return self.route_trie.handler
            
        splited_path = self.split_path(path)
        
        find_result = self.route_trie.find(splited_path)

        if find_result is None:
            return self.not_found_handler
        else:
            return find_result


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        contents = path.split('/')
        for item in contents:
            if item is '':
                contents.remove(item)
        return contents
        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# tests 1-4
# some lookups with the expected output
print(router.lookup("/")) 
# Answer:'root handler'
print(router.lookup("/home")) 
# Answer: 'not found handler'
print(router.lookup("/home/about")) 
# Answer: 'about handler'
print(router.lookup("/home/about/me")) 
# Answer: 'not found handler'

# edge test 1 - empty input
print(router.lookup("") == 'not found handler')
# Answer: 'not found handler'

# edge test 2 - non-existed page
print(router.lookup("/home/about/aslan") == 'not found handler')
# Answer: 'not found handler'