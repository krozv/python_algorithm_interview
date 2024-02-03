# 5. Longest Palindrome Substring
"""
1 <= s.length <= 1000
s is digit and english letters
"""


class LongestPalindromeSubstring:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        # plan
        # i: N -> 0
        # i 자체적으로 palindrome인지 확인
        for i in range(str_len, 0, -1):
            for j in range(str_len-i+1):
                word = s[j:j+i]
                if word == word[::-1]:
                    palindrome = word
                    return palindrome


c = LongestPalindromeSubstring()
input1 = "babab"
input2 = "c"
print(c.longestPalindrome(input1))
print(c.longestPalindrome(input2))
