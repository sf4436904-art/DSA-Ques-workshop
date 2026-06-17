class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            rev = rev * 10 + rem
            temp = temp // 10
        return rev == x


if __name__ == "__main__":
    s = Solution()
    tests = [121, -121, 10, 0, 12321]
    for t in tests:
        print(f"{t} -> {s.isPalindrome(t)}")

