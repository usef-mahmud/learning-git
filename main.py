import time
from utils import get_list

time.sleep(1)
a = int(input('range start: '))
b = int(input('range end: '))

for i in get_list(a, b):
    print(f'line number #{i}')