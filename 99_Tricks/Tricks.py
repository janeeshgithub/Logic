print(all([0,1,2,3,4,5]))
print(any([0,1,2,3,4,5]))
print(ascii("a"))
print(bool())
print(callable(int))
print(callable(100))
print(complex(90))
print(dict())
print(set())
print(dir("hello"))

a=divmod(10,4)
print(a)
source = """
def greet(name):
    return f"Hello, {name}!"

message = greet('Janeesh')
"""
exec(source)
print(message)

arr = ["a", "ab", "abba", "ads", "ge", "gtt", "fd"]
arr = filter(lambda s: s[0] == 'g', arr)
arr = list(arr)  # Convert filter object to a list
print(arr)

