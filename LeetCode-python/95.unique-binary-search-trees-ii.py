#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        stack = deque()
        stack.append(self)
        ressult = []
        while stack:
            node = stack.popleft()
            if node:
                ressult.append(node.val)
                if node.left or node.right:
                    stack.append(node.left)
                    stack.append(node.right)
            else:
                ressult.append('#')
        return '[' +','.join(map(str, ressult))+']'
                

            

from typing import List,Optional
class Solution:
    @staticmethod
    def generateSubTree(left,right):
        if left > right:
            return [None]
        if left == right:
            return [TreeNode(left)]
        res = []
        for i in range(left,right+1):
            left_subtrees = Solution.generateSubTree(left,i-1)
            right_subtrees = Solution.generateSubTree(i+1,right)
            for l in left_subtrees:
                for r in right_subtrees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return Solution.generateSubTree(1,n) if n else []
            
if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))
# @lc code=end

