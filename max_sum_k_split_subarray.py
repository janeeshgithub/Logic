def findPages(arr, k):
    if len(arr) < k:
        return -1
    def is_valid(mid):
        subarray_count = 1
        current_sum = 0
        for num in arr:
            if current_sum + num > mid:
                subarray_count += 1
                current_sum = num
                if subarray_count > k:
                    return False
            else:
                current_sum += num
        return True
    low, high = max(arr), sum(arr)
    result = high

    while low <= high:
        mid = (low + high) // 2

        if is_valid(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

arr = [1, 2, 3, 4]
k = 3
print(findPages(arr, k))  # Output: 4
