__author__ = 'lilianga'

import psutil

a = psutil.cpu_count()
print(a)
b = psutil.cpu_count(logical=False)
print(b)
