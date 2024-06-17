# dictionaries
map = {
    12: 'value1',
    'key2': [1,2,3],
    True: True
}
print(type(map))
print(map[12])
print(map.get('key2'))
print(map.get(True))
print(map.get('key4'))
print(map.get('key4', 0))

## update dictionary
map.update({12: 'value2'})
map.update({123: 'value3'})
print(map)

# tuples (immutable lists)
mytuple = (1,'apple', True, 1)
print(type(mytuple))
print(mytuple)
print(mytuple[1])

# sets (unique unordered collections)
myset = {1,2,2,4,2,4,1}
yourset = {4,5,6,7,8}
print(type(myset))
print(myset)

## set union and intersection shorthands
print(myset & yourset)
print(myset | yourset)
