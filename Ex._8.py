from itertools import *

#Каждый символ используется 1 раз, порядок важен
for i in permutations('ABC', 2):
    print(i)

print('---')

#Каждый символ используется любое количество раз, порядок важен
for i in product('ABC', repeat=2):
    print(i)

print('---')

#Каждый символ используется 1 раз, порядок не важен
for i in combinations('ABC', 2):
    print(i)
