# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        increased = []
        enough = False
        for i in range(len(digits) - 1, -1, -1):
            cur = digits[i]
            if cur == 9 and not enough:
                increased.insert(0, 0)
            elif not enough:
                increased.insert(0, cur + 1)
                enough = True
            else:
                increased.insert(0, cur)

        if increased[0] == 0:
            increased.insert(0, 1)
        return increased


if __name__ == "__main__":
    s = Solution()
    digits = [1, 2, 3, 9]
    print(s.plusOne((digits)))
