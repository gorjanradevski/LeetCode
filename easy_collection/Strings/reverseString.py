# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = tmp


if __name__ == "__main__":
    s = Solution()
    string = ["h", "e", "l", "l", "o"]
    s.reverseString((string))
    print(string)
