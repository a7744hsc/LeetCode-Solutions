#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # note: this is not a coding test
        if n>=4 and n%4==0:
            return False
        return True
        
# @lc code=end

