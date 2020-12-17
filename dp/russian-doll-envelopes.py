# Problem: Russian Doll Envelopes
# Link: https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes == None:
            return 0
        n = len(envelopes)
        print(envelopes)
        if n <= 1:
            return n
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        print(envelopes)
        
        trail = [(0,0) for x in range(n)]
        size = 0
        for envelop in envelopes:
            i, j = 0, size
            while i < j:
                m = (i + j) // 2
                if envelop[1] > trail[m][1]:
                    i = m + 1
                else:
                    j = m
            trail[i] = envelop
            size = max(size, i+1)
        return size
