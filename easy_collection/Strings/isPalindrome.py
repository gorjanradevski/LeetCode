# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list = []
        for char in s:
            if char.isalnum():
                s_list.append(char)
        size = len(s_list)
        if s_list == 0:
            return True
        for i in range(size // 2):
            if s_list[i] != s_list[-(i + 1)]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))