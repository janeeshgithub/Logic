nums = [1, 2, 3, 4, 5, 6, 3, 2]
k = 15
p = {0: -1}  # Initialize with 0 sum at index -1
cs = 0
t = 0
ml = 0  # Maximum length initialized to 0
subarrays = []  # List to store subarrays whose sum equals k

for i in range(len(nums)):
    cs += nums[i]

    if cs - k in p:
        t += 1  # Count the subarray
        subarrays.append(nums[p[cs - k] + 1:i + 1])  # Extract the subarray

        # Calculate the length of the subarray
        ml = max(ml, i - p[cs - k])

    # Update the cumulative sum with its corresponding index
    p[cs] = p.get(cs, i)

# Print the results
print("Number of subarrays whose sum equals k:", t)
print("Maximum length of subarray:", ml)
print("Subarrays with sum equal to", k, ":", subarrays)
