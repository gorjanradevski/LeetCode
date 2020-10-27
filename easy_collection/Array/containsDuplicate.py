# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for e in nums:
            unique.add(e)
        return len(unique) != len(nums)