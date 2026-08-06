class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.']*n for i in range(n)]
        path = [[0]*n for i in range(n)]
        result = []

        def updatePath(row, col, factor):
            
            # 1. Left to right (Row)
            for c in range(n):
                path[row][c] += factor

            # 2. Top to bottom (Column - skipping the intersection to avoid double-counting)
            for r in range(n):
                if r != row:
                    path[r][col] += factor

            # 3. Top-Left Diagonal (r decreases, c decreases)
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                path[r][c] += factor
                r -= 1
                c -= 1

            # 4. Top-Right Diagonal (r decreases, c increases)
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                path[r][c] += factor
                r -= 1
                c += 1

            # 5. Bottom-Left Diagonal (r increases, c decreases)
            r, c = row + 1, col - 1
            while r < n and c >= 0:
                path[r][c] += factor
                r += 1
                c -= 1

            # 6. Bottom-Right Diagonal (r increases, c increases)
            r, c = row + 1, col + 1
            while r < n and c < n:
                path[r][c] += factor
                r += 1
                c += 1


        def placeNextQueen(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            for col in range(n):
                if path[row][col] == 0:
                    board[row][col] = 'Q'
                    updatePath(row,col,1)
                    placeNextQueen(row+1)
                    board[row][col] = '.'
                    updatePath(row,col,-1)

        placeNextQueen(0)
        return result