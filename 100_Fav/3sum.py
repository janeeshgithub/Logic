def find_triplets(arr):
    arr.sort()
    n = len(arr)
    result = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]

            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1

                # Skip duplicates for j and k
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return result

# Example usage
arr = [-1, 0, 1, 2, -1, -4]
triplets = find_triplets(arr)

for triplet in triplets:
    print(f"[{', '.join(map(str, triplet))}]", end=" ")
print()
