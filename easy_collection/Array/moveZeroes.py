# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                for j in range(i, len(nums) - 1):
                    if nums[j + 1] == 0:
                        break
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)