import os
from datetime import datetime

#os.mkdir('OS-Demo-2')
#os.makedirs('OS-Demo-2')

#os.rmdir('OS-Demo-2')
#os.removedirs('OS-Demo-2')

#os.rename('test.txt', 'demo.txt')

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.stat('demo.txt').st_size)
#print(os.listdir())

# walking directory

# for dirpath, dirnames, filenames in os.walk('os.getcwd()'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# ENvironment variables
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.isdir('/tmp/test.txt'))
# print(os.path.isfile('/tmp/test.txt'))
# print(os.path.splitext('/tmp/test.txt'))

# print(dir(os.path))