# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = {}
        size = len(s)
        for i in range(size):
            if s[i] in uniques:
                uniques[s[i]] = size
            if s[i] not in uniques:
                uniques[s[i]] = i
        lowest_non_negative = size
        for pos in uniques.values():
            if pos < lowest_non_negative:
                lowest_non_negative = pos

        return -1 if lowest_non_negative == size else lowest_non_negative


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("loveleetcode"))
