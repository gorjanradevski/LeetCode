# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i]

        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(([7, 1, 5, 3, 6, 4])))
