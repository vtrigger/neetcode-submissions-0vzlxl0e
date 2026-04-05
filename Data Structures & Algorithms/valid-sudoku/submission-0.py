class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        def check_valid(element, x, y):
            for i in range(n):
                if i!=x and board[i][y]==element:
                    return False
            
            for j in range(n):
                if j!=y and board[x][j]==element:
                    return False

            m = int(n**0.5)
            box_x, box_y = x-x%m, y-y%m

            for i in range(box_x, box_x+m):
                for j in range(box_y, box_y+m):
                    if i==x and j==y:
                        continue
                    else:
                        if board[i][j]==element:
                            return False

            return True


        for i in range(n):
            for j in range(n):
                if board[i][j]=='.':
                    continue
                if not check_valid(board[i][j], i, j):
                    return False

        return True
        