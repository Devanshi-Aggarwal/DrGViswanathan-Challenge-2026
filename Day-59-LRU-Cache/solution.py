class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.join(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        self.remove(node)
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.value = value
            self.remove(node)
            self.moveToHead(node)
            return

        if len(self.keyToNode) == self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.keyToNode[node.key]

        node = Node(key, value)
        self.keyToNode[key] = node
        self.moveToHead(node)

    def remove(self, node):
        self.join(node.prev, node.next)

    def moveToHead(self, node):
        self.join(node, self.head.next)
        self.join(self.head, node)

    def join(self, left, right):
        left.next = right
        right.prev = left
