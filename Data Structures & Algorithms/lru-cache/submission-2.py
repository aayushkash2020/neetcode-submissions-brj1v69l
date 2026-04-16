# Maintain a linked list of nodes
# Each node has a key, value, prev, and next
# Maintain a mapping of key to node address
# Write functionality to remove from and append to front of linked list
# On get call, return -1 if key not in cache. Otherwise, remove key_to_node[key]
# from its position in the list, append to front, and return node.val
# On put call, check if node in cache. If it is, remove and append the node
# (same as get) and return node.val. If not, and list is at capacity, remove
# node at tail.prev (LRU node) and append new node to head

# Write simple Node class
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def set_val(self, val):
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.cap = capacity
        # Dummy tail and head
        self.tail = Node(0, 0)
        self.head = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def _append(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._remove(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key not in self.key_to_node:
            node = Node(key, value)
            if len(self.key_to_node) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.key_to_node[lru.key]
        else:
            node = self._remove(self.key_to_node[key])
            node.set_val(value)
        self.key_to_node[key] = node
        self._append(node)

