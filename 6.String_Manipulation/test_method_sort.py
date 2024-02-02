# method 'sort' test
a = ['aC', 'bB', 'cA']

a.sort(key=lambda x: x[0])
print(a) # ['aC', 'bB', 'cA']

a.sort(key=lambda x: x[1])
print(a) # ['cA', 'bB', 'aC']