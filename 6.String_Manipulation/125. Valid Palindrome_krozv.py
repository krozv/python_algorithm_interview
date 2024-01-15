import re

str1 = input()
str1.lower()
str1.strip()
str2 = re.findall(r"[A-Za-z]", str1)

print(str2[::-1] == str2)
