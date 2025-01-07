from collections import defaultdict

# Creating a defaultdict with a default value of int (default value is 0)
t= defaultdict(lambda:"HI")
t[1]=10
for i in range(10):
    if i==1:
        continue
    t[i]=None
print(t.items())  # Output: 0 (because 2 doesn't exist and defaultdict(int) gives 0 by default)
