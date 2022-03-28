#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = defaultdict(int)
        for char in s:
            char_count[char]+=1
        has_single = False
        count = 0
        for k,v in char_count.items():
            if v%2 !=0:
                has_single = True
            count += (v//2)*2
        if has_single:
            count+=1
        return count 
        
# @lc code=end

