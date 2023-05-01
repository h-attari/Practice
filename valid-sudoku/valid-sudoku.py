class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(arr):
            s = ''.join(arr).replace('.','')
            return len(s) == len(set(s))
        def checkRow():
            for row in board:
                if not isValid(row):
                    return False
            return True
        def checkCol():
            for col in zip(*board):
                if not isValid(col):
                    return False
            return True
        def checkSub():
            for r in range(0,9,3):
                for c in range(0,9,3):
                    sub = [board[r+dr][c+dc] for dr in range(3) for dc in range(3)]
                    if not isValid(sub):
                        return False
            return True
        return checkRow() and checkCol() and checkSub()