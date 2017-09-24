ab = {
    'Swaroop':'swaroop@qq.com',
    'Tony':'tony@qq.com,',
    'Mudso':'mudso@qq.com',
    'Jenny':'jenny@qq.com'
}
print('Swaroop\'s address is',ab['Swaroop'])

del ab['Jenny']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('contact {} at {} '.format(name,address))

ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])