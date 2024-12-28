def subarray_sum_with_hashmap(nums, target):
    prefix_sum_counts = {0: 1}  # Dictionary to store the count of prefix sums
    prefix_sum = 0
    result = 0

    for num in nums:
        prefix_sum += num
        result += prefix_sum_counts.get(prefix_sum - target, 0)
        prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1
        print(prefix_sum_counts)
    return result

# Example Usage
nums = [1, 2, 3, -2,-5,0,3,0]
target = 6
p=subarray_sum_with_hashmap(nums, target)
print()
print(p)# Output: Number of subarrays with sum = target
