class Palindrom:
    def is_palidrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalpha():
                strs.append(char.upper())
        print(strs)
        return strs == strs[::-1]


s = "A man, a plan, a canal: Panama"
c = Palindrom()
print(c.is_palidrome(s))