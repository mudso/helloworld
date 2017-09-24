import os
import time

source = ['"C:\\my document"']
backup_dir = 'D:\\backup'

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

today = backup_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_'+ \
        comment.replace(' ','_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
zip_command = "zip -r {0} {1}".format(target,
                                      ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')