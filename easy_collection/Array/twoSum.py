# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hashmap:
                return [hashmap[remain], i]
            hashmap[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
