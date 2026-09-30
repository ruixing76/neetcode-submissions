class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not len(board) or not len(board[0]):
            return False
        m=len(board)
        n=len(board[0])
        valid_square=defaultdict(set)

        # check row
        for i in range(m):
            valid_col=set()
            for j in range(n):
                if board[i][j]!='.':
                    if board[i][j] not in valid_col:
                        valid_col.add(board[i][j])
                    else:
                        return False
        # check column
        for j in range(n):
            valid_row=set()
            for i in range(m):
                if board[i][j]!='.':
                    if board[i][j] not in valid_row:
                        valid_row.add(board[i][j])
                    else:
                        return False

        # check square
        for i in range(m):
            for j in range(n):
                idx=(i//3)*3+(j//3)
                if board[i][j]!='.':
                    if board[i][j] not in valid_square[idx]:
                        valid_square[idx].add(board[i][j])
                    else:
                        return False
        return True