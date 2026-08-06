
class Node:
    def __init__(self) -> None:
        self.trie: dict[str, Node] = {}
        self.is_end_of_word: bool = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node  = self.root
    
        for ch in word:

            if( ch not in node.trie):
                node.trie[ch] = Node()

            node = node.trie[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:

        node = self.root

        for ch in word:
            if ch not in node.trie:
                return False
            node = node.trie[ch]

        return node.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for ch in prefix:
            if ch not in node.trie:
                return False
            node = node.trie[ch]

        return True    

        
        