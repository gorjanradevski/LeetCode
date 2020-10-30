# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/


class Solution:
    def reverse(self, x: int) -> int:
        if x // 10 == 0:
            return x
        x_str = str(x)
        # take the sign
        sign = False
        if x_str[0] == "-":
            sign = True
            x_str = x_str[1:]
        # reverse the string
        x_str = x_str[::-1]
        # strip starting zeros
        i = 0
        while x_str[i] == "0":
            i += 1
        x_str = x_str[i:]
        # return the sign
        reversed_int = int(x_str)
        if sign:
            reversed_int *= -1
        if reversed_int >= 0x7FFFFFFF or reversed_int <= -0x80000000:
            return 0
        return reversed_int


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(12300))
