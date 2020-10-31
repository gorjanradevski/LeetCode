# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_n = len(needle)
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i : i + size_n] == needle:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    haystack = "abc"
    needle = "bc"
    print(s.strStr(haystack, needle))