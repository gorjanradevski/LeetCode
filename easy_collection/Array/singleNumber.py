# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for e in nums:
            if e not in hashset:
                hashset.add(e)
            else:
                hashset.remove(e)
        return hashset.pop()


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
    print(s.singleNumber((nums)))
