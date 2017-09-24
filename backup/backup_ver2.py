import os
import time

source = ['"C:\\my document"']

target_dir = 'D:\\backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime('%Y%m%d')
    # 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')