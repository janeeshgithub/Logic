
# def min_partition_difference(n, parcels):
#     total_sum = sum(parcels)
#     target = total_sum // 2
#
#     # DP array: Can we form a sum 'j' using first 'i' items?
#     dp = [False] * (target + 1)
#     dp[0] = True  # Base case: We can always form sum 0
#
#     for parcel in parcels:
#         # Traverse backwards to avoid using the same item multiple times
#         for j in range(target, parcel - 1, -1):
#             dp[j] |= dp[j - parcel]
#
#     # Find the largest S1 ≤ total_sum//2 that is possible
#     for s1 in range(target, -1, -1):
#         if dp[s1]:
#             return abs(total_sum - 2 * s1)
#
#
# # Input handling
# n = int(input())
# parcels = list(map(int, input().split()))
#
# # Compute and print result
# print(min_partition_difference(n, parcels))
