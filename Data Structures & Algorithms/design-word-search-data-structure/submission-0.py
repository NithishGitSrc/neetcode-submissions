class Node:
    def __init__(self):
        # Fixed syntax error: changed colon to equals sign for dictionary initialization
        self.trie: dict[str, 'Node'] = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.trie:
                node.trie[ch] = Node()
            node = node.trie[ch]
        # FIX 1: Mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root

        def wildCardSearch(root, indx):
            node = root
            
            while indx < len(word):
                ch = word[indx]
                if ch != "." and ch not in node.trie:
                    return False
                
                if ch == ".":
                    # FIX 2: Check all matching paths without corrupting the loop's 'node' variable
                    for key in node.trie:
                        if wildCardSearch(node.trie[key], indx + 1):
                            return True
                    return False
                
                node = node.trie[ch]
                indx += 1 # Move index forward in the loop
            
            # FIX 3: Check if the final node is actually a completed word
            return node.is_end_of_word

        return wildCardSearch(node, 0)
