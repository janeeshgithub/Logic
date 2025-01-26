
# def rec(arr,st,cur):
#     if st==len(arr):
#         print(cur)
#         return
#     cur.append(arr[st])
#     rec(arr,st+1,cur)
#     cur.pop()
#     rec(arr,st+1,cur)
#
# rec([1,2,3,4],0,[])
# # print(k)


def knapsack(weights, values, W, n):
    if n == 0 or W == 0:
        return 0
    if weights[n - 1] > W:
        return knapsack(weights, values, W, n - 1)
    take = values[n - 1] + knapsack(weights, values, W - weights[n - 1], n - 1)  # Take
    not_take = knapsack(weights, values, W, n - 1)
    return max(take, not_take)

# Example usage
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
W = 8
n = len(weights)
print(knapsack(weights, values, W, n))  # Output: 110
