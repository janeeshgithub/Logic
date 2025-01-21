from bisect import *
class Solution(object):
    def maxEnvelopes(self, envelopes):
        n=len(envelopes)
        tail = []
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        for i,j in envelopes:
            pos = bisect_left(tail, j)
            if pos == len(tail):
                tail.append(j)
            else:
                tail[pos] = j
        return len(tail)