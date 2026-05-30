class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        ROWS = len(board)
        COLS = len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                elif (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[tuple([r // 3, c // 3])]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[tuple([r//3, c//3])].add(board[r][c])
        
        return True