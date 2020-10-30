# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1
        for char in t:
            if char not in chars:
                return False
            chars[char] -= 1
        for char in chars.keys():
            if chars[char] != 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("silent", "listen"))
