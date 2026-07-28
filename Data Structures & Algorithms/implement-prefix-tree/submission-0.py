class Node:
    def __init__(self):
        self.children = dict() # pointer to other Nodes

class PrefixTree:
    def __init__(self):
        self.head = Node()        
    def insert(self, word: str) -> None:
        curr = self.head
        length = 0
        while length < len(word):
            if word[length] not in curr.children:
                nd = Node()
                curr.children[word[length]] = nd
            curr = curr.children[word[length]]
            length += 1
        curr.children[None] = None

    def search(self, word: str) -> bool:
        curr = self.head
        length = 0
        while length < len(word):
            if word[length] not in curr.children:
                return False
            curr = curr.children[word[length]]
            length += 1

        return None in curr.children

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        length = 0
        while length < len(prefix):
            if prefix[length] not in curr.children:
                return False
            curr = curr.children[prefix[length]]
            length += 1
        
        return True
        