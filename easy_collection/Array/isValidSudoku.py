# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Square sets
        unique_f = set()
        unique_s = set()
        unique_t = set()
        for i in range(9):
            # Row and column sets
            unique_row = set()
            unique_column = set()
            # Square sets
            if i % 3 == 0:
                unique_f = set()
                unique_s = set()
                unique_t = set()
            for j in range(9):
                e_row = board[i][j]
                e_col = board[j][i]
                # Check square
                if j < 3:
                    if e_row in unique_f:
                        return False
                    if e_row != ".":
                        unique_f.add(e_row)
                elif j < 6:
                    if e_row in unique_s:
                        return False
                    if e_row != ".":
                        unique_s.add(e_row)
                else:
                    if e_row in unique_t:
                        return False
                    if e_row != ".":
                        unique_t.add(e_row)
                # Check row
                if e_row in unique_row:
                    return False
                if e_row != ".":
                    unique_row.add(e_row)
                # Check column
                if e_col in unique_column:
                    return False
                if e_col != ".":
                    unique_column.add(e_col)

        return True


if __name__ == "__main__":
    s = Solution()
    board_1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board_2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(s.isValidSudoku(board_1))
