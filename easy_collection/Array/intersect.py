# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elem2count = {}
        for elem in nums1:
            if elem not in elem2count:
                elem2count[elem] = 0
            elem2count[elem] += 1

        intersect = []
        for elem in nums2:
            if elem in elem2count:
                if elem2count[elem] > 0:
                    intersect.append(elem)
                elem2count[elem] -= 1

        return intersect


if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    s = Solution()
    print(s.intersect(nums1, nums2))