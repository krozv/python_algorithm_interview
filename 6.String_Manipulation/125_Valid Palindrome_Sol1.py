class IsPalindrome:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            # isalnum() - method returns True if all the characters
            # are alphanumeric, meaning alphabet letter and numbers(0-9)
            if char.isalnum():
                strs.append(char.lower())

            while len(strs) > 1:
                if strs.pop(0) != strs.pop():
                    return False

            return True


a = IsPalindrome()
s = 'A man, a plan, a canal: Panama'
print(a.isPalindrome(s))