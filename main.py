import time
from utils import get_list, get_len

time.sleep(1)
a = int(input('range start: '))
b = int(input('range end: '))

for i in get_list(a, b):
    print(f'line number #{i}')

print(f'the length is {get_len(get_list(1,10))}')