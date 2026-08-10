class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c, root, word):
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r,c) in visit or board[r][c] not in root.children):
                return
            
            visit.add((r,c))
            root = root.children[board[r][c]]
            word+= board[r][c]
            
            if root.isWord:
                res.add(word)

            dfs(r-1, c , root, word)
            dfs(r+1, c , root, word)
            dfs(r, c+1 , root, word)
            dfs(r, c-1 , root, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c , root , "" )

        return list(res)
