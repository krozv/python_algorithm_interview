# Using Deque
class Palindrom:

    def isPalindrom(self, s: str) -> bool:
        import collections
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


f = Palindrom()
input = "A man, a plan, a canal: Panama"
print(f.isPalindrom(input))