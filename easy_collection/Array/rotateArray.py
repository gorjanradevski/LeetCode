# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

from typing import List


class Solution:
    # O(n) space, O(n) speed
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        rotated = [0] * length
        for i in range(length):
            rotated[(i + k) % length] = nums[i]

        nums[:] = rotated

    # O(1) space, O(n * k) speed
    def rotate_brute(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            self.shift_right_brute(nums)

    def shift_right_brute(self, nums: List[int]):
        for i in range(len(nums) - 1, 0, -1):
            tmp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = tmp


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    s.rotate(nums, 3)
    print(nums)
