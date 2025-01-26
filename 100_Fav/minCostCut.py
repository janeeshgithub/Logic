class Solution(object):
    def minCost(self, n, cuts):
        mem = {}

        def dfs(l, r):
            if r - l == 1:
                return 0
            if (l, r) in mem:
                return mem[(l, r)]
            a = float('inf')
            for k in cuts:
                if l < k < r:
                    a = min(a, (r - l) + dfs(l, k) + dfs(k, r))
            a = 0 if a == float('inf') else a
            mem[(l, r)] = a
            return mem[(l, r)]

        return dfs(0, n)

