class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9): # vertical
            seen = set()
            for j in range(9): # horizontal
                if board[i][j] != ".":
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        return False

        # check col
        for i in range(9): # horizontal 
            seen = set()
            for j in range(9): # vertical
                if board[j][i] != ".":
                    if board[j][i] not in seen:
                        seen.add(board[j][i])
                    else:
                        return False    

        # check box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for y in range(i, i + 3):
                    for x in range(j, j + 3):
                        if board[x][y] != ".":
                            if board[x][y] not in seen:
                                seen.add(board[x][y])
                            else:
                                return False

        return True

