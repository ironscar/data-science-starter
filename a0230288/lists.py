## Lists
print('\nLists:')

list = [1,2,'a', 'b', True, False]
print('List = ' + str(list))
print('Element 0 = ' + str(list[0]))
print('Type of Element 0 = ' + str(type(list[0])))
print('Length = ' + str(len(list)))

## list slicing
sublist = list[0:4:2]
print(sublist)
copylist = list[:]
print(copylist)

## list mutability
samereflist = list
samereflist[0] = 'apple'
list[1] = 5
copylist[2] = 3
print(list)

## matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][0])