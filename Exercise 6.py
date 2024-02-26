# String are immutable
s = "hello"
print(s[0])
s[0] = "y"
s2 = "y" + s[1:]
print(s2)

# Lists are mutable
l = [1, 2, 3, 4]
print(l[0])
l[0] = 5
print(l)
