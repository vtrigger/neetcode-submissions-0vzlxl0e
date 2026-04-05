class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        def rows_valid():
            for row in board:
                checker = [0 for _ in range(n)]

                for num in row:
                    if num=='.':
                        continue
                    else:
                        num = int(num)
                    if checker[num-1]==0:
                        checker[num-1] = num
                    else:
                        return False

            return True


        def cols_valid():
            for j in range(n):
                checker = [0 for _ in range(n)]

                for i in range(n):
                    if board[i][j]=='.':
                        continue
                    else:
                        board[i][j] = int(board[i][j])

                    if checker[board[i][j]-1]==0:
                        checker[board[i][j]-1] = board[i][j]
                    else:
                        return False

            return True
        
        def boxes_valid():
            m = int(n**0.5)

            for box in range(n):
                checker = [0 for _ in range(n)]

                for i in range(m):
                    for j in range(m):
                        x, y = i+m*(box//m), j+m*(box%m)
                        if board[x][y]=='.':
                            continue
                        else:
                            board[x][y] = int(board[x][y])

                        if checker[board[x][y]-1]==0:
                            checker[board[x][y]-1] = board[x][y]
                        else:
                            return False

            return True


        return rows_valid() and cols_valid() and boxes_valid()