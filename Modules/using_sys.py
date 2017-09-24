import sys
print('the command line argument are:')
for i in sys.argv:
    print (i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')

from math import sqrt
print('square root of 16 is',sqrt(16))