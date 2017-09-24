try:
    text = input('Enter something -->')
except EOFError:
    print('why did you do an EOFon me')
except KeyboardInterrupt:
    print('you canelled the operation')
else:
    print('you entered {}'.format(text))