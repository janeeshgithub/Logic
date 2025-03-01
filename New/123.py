from logging import exception

import Zzm3
from New.Zzm3 import Janeesh


class A:
    def __init__(self):
        print("AK")
class B(A):
    def __init__(self):
        super().__init__()
az=A()
b=B()
a=Janeesh(1,2)
a.eats()

match():
    case 1:
        print("0-")
    case 10:
        print("100-")
    case 0:
        print("sdsdsd")
print('--'*15)
try:
    print(10 // 0)  # This will raise a ZeroDivisionError
except Exception as e:  # Use `except` instead of `catch`
    print(e)