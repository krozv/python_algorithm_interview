class ReverseString:
    def reverse_string(self, str_list) -> None:
        str_list = str_list[::-1]
        print(id(str_list), id(str_list[:]), id(str_list[::-1]))

c = ReverseString()
input = ['h', 'e', 'l', 'l', 'o']
c.reverse_string(input)
print(input)
