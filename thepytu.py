# -*- coding: utf-8 -*-
import json

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")  # this is the first comment

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
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, ' is a prime number.')


def fib(n):
    """Print a Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end='\t')
        a, b = b, a + b
    print()


fib(20000)
f = fib
f(2000)
print(type(f), type(fib))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """A function with default argument values"""
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('Do you want biuld a snowman?', 1)

def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "asian", "china"))

# args_ok = ('Do you?\n', 2)
# ask_ok(*args_ok)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouln't", action, end=' ')
    print("If you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(43)
print(f(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1][1])
print(pairs)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

with open('test', 'w+') as f:
    x = json.dumps([1, 'hello'])
    print(x)
    json.dump(x, f)
    # y = json.load(f)
    # print(y)
f.close()

while True:
    try:
        x = int(input('Pls enter a number: '))
        break
    except ValueError:
        print("Oop! That was no valid number. Try again...")