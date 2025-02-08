from collections import defaultdict


class Solution:
    def maxLength(self, arr):

        # defaultdict to calculate the
        # frequency of each element
        freq = defaultdict(int)
        for x in arr:
            freq[x] += 1

        # List to store elements of array and its frequency
        v = [(key, value) for key, value in freq.items()]

        # defaultdict to store number of
        # planks of particular length
        sum = defaultdict(int)

        # Storing frequency of planks of all possible lengths
        for i in range(len(v)):
            plankLen = v[i][0]
            plankFreq = v[i][1]

            # Increasing the number of planks
            # of length plankLen in hash map
            sum[plankLen] += plankFreq

            # Increasing the number of planks of
            # length 2*plankLen in hash map
            sum[plankLen * 2] += plankFreq // 2

            # Increasing the number of planks
            # of length (plankLen + v[j][0]) in hash map
            for j in range(i + 1, len(v)):
                sum[v[j][0] + plankLen] += min(v[j][1], plankFreq)

        # Storing maximum frequency of planks
        # of all possible lengths
        res = 0
        for value in sum.values():
            res = max(res, value)

        return res - 1