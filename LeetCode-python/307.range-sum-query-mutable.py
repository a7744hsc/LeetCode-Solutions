#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (38.60%)
# Likes:    2660
# Dislikes: 143
# Total Accepted:    178.3K
# Total Submissions: 461.7K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, handle multiple queries of the following
# types:
# 
# 
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
# 
# 
# Implement the NumArray class:
# 
# 
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be
# val.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
# 
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 10^4 calls will be made to update and sumRange.
# 
# 
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.binary_indexed_tree = [0]*len(nums)
        self.origin_list = [0]*len(nums)
        for i,n in enumerate(nums):
            self.update(i,n)
        

    def update(self, index: int, val: int) -> None:
        delta = val - self.origin_list[index]
        self.origin_list[index] = val
        if index ==0:
            self.binary_indexed_tree[0]= val
            index+=1
        while index<len(self.binary_indexed_tree):
            self.binary_indexed_tree[index]+=delta
            index = index + (index&-index)

    def sumRange(self, left: int, right: int) -> int:
        if right ==0:
            return self.binary_indexed_tree[0]
        result = 0
        if left>0:
            if left ==1:
                result-=self.binary_indexed_tree[0]
            else:
                left = left-1
                while left>0:
                    result-=self.binary_indexed_tree[left]
                    left-=(left&-left)
            
        while right>0:
            result+=self.binary_indexed_tree[right]
            right-=(right&-right)
        
        return result




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

