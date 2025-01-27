fs=frozenset([1,3,4,1,2,4])
print(fs)
print(hash(fs))
print(globals())
print(locals())
# print(help())
# help(print)
print(id(10))
print(isinstance(1.0,float ))
class A:
    pass
class B(A):
    pass
print(issubclass(A,B))
print(issubclass(B,A))
print(repr('3'))
text = "janeesh"
utf8_encoded = text.encode('utf-8')
print(list(utf8_encoded))  # Byte values
print(utf8_encoded.hex())
import datetime from datetime

dt=datetime.now()
Jan=100_000_000
print(f'False{Jan:_.1f}False')

