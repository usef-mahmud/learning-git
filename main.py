import time
from utils import get_list, get_len

time.sleep(1)
a = int(input('range start: '))
b = int(input('range end: '))

for i in get_list(a, b):
    print(f'line number #{i}')

print(f'the length is {get_len(get_list(1,10))}')

for i in range(10):
    print(f'timer #{i}')
    time.sleep(1)

for i in get_list(1,10):
    print(f'long timer #{i}')
    time.sleep(10)
print('a test')

# it's a comment in the master branch
# another comment
# other line