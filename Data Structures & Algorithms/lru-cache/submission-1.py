class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # 1. define the left and right outside pointers
        # 2. size of the LRU cache
        # 3. make sure the left and right pointers are connected
        # to each other

        # On this question we will just treat the lefthandside being the least recently
        # used, and the rightside as the most recently seen nodes

        self.capacity = capacity
        self.cache = {} # key -> node
        self.left = Node(0,0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # We just delete the node we reference
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # add the node on the righthand side
        prev_right = self.right.prev
        prev_right.next = node
        node.prev = prev_right
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if(key in self.cache):
            node = self.cache[key]
            node_val = node.value
            self.remove(node)
            self.insert(node)
            return node_val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if(len(self.cache) > self.capacity):
            # remove from the left handside
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]

        


