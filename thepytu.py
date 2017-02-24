# -*- coding: utf-8 -*-
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!") #this is the first comment

text = "# This is not a comment because it's inside quotes."
print(text)

width = 20
height = 5 * 9
print(width * height)
print(3 * 3.75 / 1.5)
print(round(float(height) / 4, 2))

stregg = 'spam eggs'
print(stregg * 8)
print('does\'nt')
print('yes,\n i do it')
print(r'C:\some\name')
print('C:\some\name')
print("""\
Usage: thingy[OPTIONS}
    -h
    -H hostname
""")
word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[0:2] + word[2:])
print(len(word))

squares = [1, 4, 9, 16, 25]
print(squares)
squares.append(36)
squares.append(7 ** 2)
print(squares)
squares[0:2] = []
print(squares)
print(len(squares))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

