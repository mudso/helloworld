age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('why is {0} playing with that python'.format(name))
print(name + 'is' + str(age) +'years old')
#格式化，从其他信息中构建字符串
print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

print('a',end=' ')
print('b',end=' ')
print('c',end=' ')
#z转义序列，用反斜杠来制定单引号
print('this is the first line\nthis is second line')
print("this is the first sentence. \
this is the second sentence")
print(r"nelines are indicated by \n")#原始字符串

