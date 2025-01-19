nums=[1,2,4,5,6]
dp = 1 << 0
target=sum(nums)//2
print(dp)
for num in nums:
    dp |= dp << num
    print(dp)
print((dp & (1 << target)) != 0)