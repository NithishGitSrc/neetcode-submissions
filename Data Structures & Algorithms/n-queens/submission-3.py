class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]
        
        # Track locked lines in O(1) time
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        def placeNextQueen(r):
            # Base Case: All queens placed successfully
            if r == n:
                result.append(["".join(row) for row in board])
                return

            for c in range(n):
                # O(1) check if the cell is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place Queen & Add to sets
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                # Move to next row
                placeNextQueen(r + 1)

                # Backtrack: Remove Queen & Clear sets
                board[r][c] = '.'
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        placeNextQueen(0)
        return result
