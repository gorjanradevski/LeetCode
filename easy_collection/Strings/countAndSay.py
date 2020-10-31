# https://leetcode.com/problems/count-and-say/
from typing import List


class Solution:
    def say(self, cur_says: List[int]):
        new_says = []
        i = 0
        while i < len(cur_says):
            count_cur = 0
            court_cur_index = i
            while (
                court_cur_index < len(cur_says)
                and cur_says[court_cur_index] == cur_says[i]
            ):
                count_cur += 1
                court_cur_index += 1
            new_says += [str(count_cur), cur_says[i]]
            i = court_cur_index
        return new_says

    def countAndSay(self, n: int) -> str:
        says = ["1"]
        for _ in range(n - 1):
            says = self.say(says)

        return "".join(says)


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(6))