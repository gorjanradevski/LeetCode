# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_repr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                str_repr.append("FizzBuzz")
            elif i % 3 == 0:
                str_repr.append("Fizz")
            elif i % 5 == 0:
                str_repr.append("Buzz")
            else:
                str_repr.append(str(i))

        return str_repr