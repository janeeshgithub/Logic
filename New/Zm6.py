class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # HashMap to store key-node pairs
        # Dummy head and tail nodes to simplify boundary conditions
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Removes a node from the DLL."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Adds a node right after the head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the accessed node to the front
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            # If the key exists, update the value and move it to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove the least recently used node (tail's previous node)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Add the new node to the front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
