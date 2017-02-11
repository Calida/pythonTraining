# Die Liste selbst wird als "List value" bezeichnet ['a', 'b'] ist also ein List value

print([1, 2, 3] + ['a', 'b', 'c'])

print(['d', 'b', 'v']*3)

spam = [1, 2, 3]
spam = spam + ['a', 'b', 'c']
print(spam)

spam = ['cat', 'spam', 'rat', 'elephant']
print(spam)
del spam[2]
print(spam)


supplies = ['pens', 'staples', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print(supplies[i])