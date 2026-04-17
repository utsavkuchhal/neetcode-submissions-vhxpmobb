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

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.get_key(char):
                curr.set_key(char)
            curr = curr.get_key(char)
        curr.set_end()

    def dfs(self, index, node, word):
        if index == len(word):
            return node.is_end

        char = word[index]
        if char == '.':
            for child in node.children:
                if child and self.dfs(index + 1, child, word):
                    return True
            return False
        
        node = node.get_key(char)
        if not node:
            return False
        
        return self.dfs(index + 1, node, word)

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)
