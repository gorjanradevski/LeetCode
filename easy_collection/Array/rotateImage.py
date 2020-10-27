# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                # print(i, j, "=", n - j - 1, i)
                matrix[i][j] = matrix[n - j - 1][i]
                # print(n - j - 1, i, "=", n - i - 1, n - j - 1)
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                # print(n - i - 1, n - j - 1, "=", j, n - i - 1)
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                # print(j, n - i - 1, "=", i, j)
                matrix[j][n - i - 1] = temp
                # print("------------------")


if __name__ == "__main__":
    s = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(matrix)
    print(matrix)