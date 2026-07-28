class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False
class WordDictionary:
    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:        
        curr = self.head
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_end = True

    def searchhelper(self, word, curr):
        for i, ch in enumerate(word):
            if ch == '.':
                for child_node in curr.children.values():
                    if self.searchhelper(word[i+1:], child_node):
                        return True
                return False
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end
        
    def search(self, word: str) -> bool:
        return self.searchhelper(word, self.head)
