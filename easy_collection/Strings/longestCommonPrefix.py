# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = "a" * 201
        for string in strs:
            if len(string) < len(shortest):
                shortest = string
        prefix = ""
        for i in range(len(shortest), 0, -1):
            found = True
            for string in strs:
                if shortest[:i] != string[:i]:
                    found = False
                    break
            if found:
                prefix = shortest[:i]
                break
        return prefix


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flozz"]))
