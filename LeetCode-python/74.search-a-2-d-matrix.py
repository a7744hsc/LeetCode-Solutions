#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for inner_list in matrix:
            if target>=inner_list[0] and target<=inner_list[-1]:
                return target in inner_list
        return False
            
# @lc code=end

