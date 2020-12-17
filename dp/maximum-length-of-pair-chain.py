# Problem: Maximum Length of Pair Chain
# Link: https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        chain = []
        if pairs == None or len(pairs) == 0:
            return chain
        if len(pairs) == 1:
            return pairs
        
        trail = [(0,0) for x in range(len(pairs))]
        pairs.sort(key = lambda x: x[0])
        
        size = 0
        for pair in pairs:
            i, j = 0, size
            discard = False
            while i < j:
                m = (i+j) // 2
                if pair[0] > trail[m][1]:
                    i = m+1
                else:
                    if  trail[m][1] < pair[1]:
                        discard = True
                        
                    else:
                        j = m
            if discard:
                continue
            trail[i] = pair
            if i == size or i == size-1:
                chain.append(pair)
            size = max(size, i+1)
        if size == 0:
            return 1
        return size