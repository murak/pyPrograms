# Leet code problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j,length = 0,0
        t = {}
        for i in range(len(s)):
            if s[i] in t:
                j = max(j,t[s[i]] + 1)
            t[s[i]] = i
            length = max(length, i-j+1)
        return length