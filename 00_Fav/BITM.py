a,b=3,5
a=a^b
print(a,b)
b=a^b
print(a,b)
a=a^b
print(a,b)
k=16
print(k&(k-1))
count = 0
n=15
while n:
    count += n & 1
    n >>= 1
print(count)
def clear_bit(n, pos):
    mask = ~(1 << pos)
    return n & mask

print(clear_bit(5, 0))  # Output: 4 (Binary: 101 -> 100)
def set_bit(n, pos):
    mask = 1 << pos
    return n | mask

print(set_bit(5, 1))  # Output: 7 (Binary: 101 -> 111)
def toggle_bit(n, pos):
    mask = 1 << pos
    return n ^ mask

print(toggle_bit(5, 0))  # Output: 4 (Binary: 101 -> 100)
def rightmost_set_bit(n):
    return n & -n

print(rightmost_set_bit(10))  # Output: 2 (Binary: 1010 -> 0010)

def is_bit_set(n, pos):
    return (n & (1 << pos)) != 0

print(is_bit_set(5, 2))  # Output: True (Binary: 101)
print(is_bit_set(5, 1))  # Output: False
