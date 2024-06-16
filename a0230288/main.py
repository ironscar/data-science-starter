## Input + Output
a =  input('Enter number: ')
print('hello ' + a)

## Rapid assignment
b,c,d = 4,5.0,'hi'
print(b)
print(c)
print(d)

## int
b = 2 ** 3
print(type(b))
print(b)

## float
b = 6 // 4.5
print(type(b))
print(b)

## Functions
print('round result')
print(round(3.10333, 2))

## string concatenation
print('\nString concatenation:')
a += ' & Dina'
print(a)
print('*' * 5)

## type casting
print('\nType casting:')
b = '100'
print(45 + int(b))
c = 100
print('Hi' + str(c))

## formatted strings
print(f'\nFormmated strings = You are {a} and the number is {c}\n')

## string indexing
print('\nString indexing:')
print('Index 0 = ' + a[0])
print('Index 1 to 4 = ' + a[1:4])
print('Index 1 to 6 stepping over 2 = ' + a[1:6:2])
print('Reverse string = ' + a[::-1])