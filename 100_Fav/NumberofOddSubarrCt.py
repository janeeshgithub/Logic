
def numberOfSubarrays(nums, k):
    l = 0  # Left pointer
    count = 0  # Number of odd numbers in the window
    subarrays = 0  # Result: number of subarrays with exactly k odd numbers
    prefixCount = 0  # Tracks how many subarrays have the same count of odd numbers

    for r in range(len(nums)):
        if nums[r] % 2 != 0:
            count += 1  # Increment odd number count
            prefixCount = 0

        # Shrink the window from the left until count == k
        while count == k:
            if nums[l] % 2 != 0:
                count -= 1  # Reduce odd count when moving left pointer past an odd number
            prefixCount += 1
            #print(prefixCount)
            l += 1

        # Add prefixCount to subarrays (valid subarrays ending at r)
        subarrays += prefixCount
        print(prefixCount)

    print(subarrays)

numberOfSubarrays([2,2,2,1,2,2,1,2,2,1,2],3)