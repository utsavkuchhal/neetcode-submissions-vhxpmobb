class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node_map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def delete_node(self, node: Node):
        curr_next = node.nxt
        curr_prev = node.prev
        curr_prev.nxt = curr_next
        curr_next.prev = curr_prev

    def put_first(self, node):
        head_next = self.head.nxt
        self.head.nxt = node
        node.prev = self.head
        node.nxt = head_next
        head_next.prev = node

    # def put_last(self, node):
    #     last_node = self.tail.prev
    #     last_node.nxt = node
    #     node.prev = last_node
    #     node.nxt = self.tail
    #     self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1
        node = self.key_node_map[key]
        if self.head.nxt != node:
            self.delete_node(node)
            self.put_first(node)
        return node.val
            
    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.val = value
            self.delete_node(node)
        else:
            node = Node(key, value)
            self.key_node_map[key] = node
            
        self.put_first(node)

        if len(self.key_node_map) > self.capacity:
            node = self.tail.prev
            self.delete_node(node)
            del self.key_node_map[node.key]


