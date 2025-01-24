nums = [1, 2, 3, 4, 5, 6, 3, 2]
k = 15
cumulative_sum = 0
subarray_count = 0
max_length = 0
prefix_sum_indices = {0: -1}  # Maps cumulative sum to its earliest index
subarrays = []  # List to store subarrays whose sum equals k

for index, num in enumerate(nums):
    cumulative_sum += num

    # Check if a subarray with sum k exists
    if cumulative_sum - k in prefix_sum_indices:
        start_index = prefix_sum_indices[cumulative_sum - k] + 1
        subarrays.append(nums[start_index:index + 1])  # Store the subarray
        subarray_count += 1  # Increment subarray count
        max_length = max(max_length, index - prefix_sum_indices[cumulative_sum - k])  # Update max length

    # Update the prefix sum map with the current cumulative sum
    if cumulative_sum not in prefix_sum_indices:
        prefix_sum_indices[cumulative_sum] = index

# Print the results
print("Number of subarrays whose sum equals k:", subarray_count)
print("Maximum length of subarray:", max_length)
print("Subarrays with sum equal to", k, ":", subarrays)
