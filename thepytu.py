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

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
# x = int(input("Please Enter An Integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

for i in range(5):
    print(i)
print(range(10))
print(list(range(10)))

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, ' is a prime number.')

