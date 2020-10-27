# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i + 1]
                index += 1

        return index


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5]
    index = s.removeDuplicates(nums)
    print(nums[:index])
