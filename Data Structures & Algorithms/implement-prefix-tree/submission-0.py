class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def contains_key(self, char):
        return self.children[ord(char) - 'a'] != None
    
    def set_key(self, char):
        self.children[ord(char) - ord('a')] = Node()

    def get_key(self, char):
        return self.children[ord(char) - ord('a')]

    def set_end(self):
        self.is_end = True
    
class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.get_key(char):
                curr.set_key(char)
            curr = curr.get_key(char)
        curr.set_end()

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            next_key = curr.get_key(char)
            if not next_key:
                return False
            curr = next_key
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            next_key = curr.get_key(char)
            if not next_key:
                return False
            curr = next_key
        return bool(curr)
        