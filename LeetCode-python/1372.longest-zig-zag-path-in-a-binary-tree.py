#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        nodes = [root]
        cache = {}
        max_len = 0
        while nodes:
            node = nodes.pop()
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            length = max(self._longestZigZag(node,True,cache),self._longestZigZag(node,False,cache))
            if length>max_len:
                max_len = length
            
        return max_len


    def _longestZigZag(self, root,is_left, cache):        
        if (root,is_left) in cache:
            return cache[(root,is_left)]
        
        if is_left:
            result = self._longestZigZag(root.left,False,cache)+1 if root.left else 0
            cache[(root,is_left)] = result
            return result
        else:
            result =  self._longestZigZag(root.right,True,cache)+1 if root.right else 0
            cache[(root,is_left)] = result
            return result
            
        
        
# @lc code=end
