# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Without new memory
        size = len(s)
        if size == 0:
            return True
        i = 0
        j = size - 1
        while i < size and j >= 0:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("race a car"))