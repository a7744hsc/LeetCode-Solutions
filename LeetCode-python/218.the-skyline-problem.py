#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (38.53%)
# Likes:    3715
# Dislikes: 193
# Total Accepted:    202.6K
# Total Submissions: 525.5K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Given the locations and
# heights of all the buildings, return the skyline formed by these buildings
# collectively.
# 
# The geometric information of each building is given in the array buildings
# where buildings[i] = [lefti, righti, heighti]:
# 
# 
# lefti is the x coordinate of the left edge of the i^th building.
# righti is the x coordinate of the right edge of the i^th building.
# heighti is the height of the i^th building.
# 
# 
# You may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# The skyline should be represented as a list of "key points" sorted by their
# x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
# endpoint of some horizontal segment in the skyline except the last point in
# the list, which always has a y-coordinate 0 and is used to mark the skyline's
# termination where the rightmost building ends. Any ground between the
# leftmost and rightmost buildings should be part of the skyline's contour.
# 
# Note: There must be no consecutive horizontal lines of equal height in the
# output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is
# not acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...,[2 3],[4 5],[12 7],...]
# 
# 
# Example 1:
# 
# 
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in
# figure B represent the key points in the output list.
# 
# 
# Example 2:
# 
# 
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1
# buildings is sorted by lefti in non-decreasing order.
# 
# 
#

# @lc code=start
import heapq
from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        critical_points = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        result, height_till_uninclusive_heap = [],[]
        for x, negH, R in critical_points:
            # remove all info on the left of x
            while height_till_uninclusive_heap and x >= height_till_uninclusive_heap[0][1]:
                heapq.heappop(height_till_uninclusive_heap)

            #when left of the building
            if negH:
                heapq.heappush(height_till_uninclusive_heap, (negH, R))
                # if result not empty or current max height != previous height;
                if not result or result[-1][1] != -height_till_uninclusive_heap[0][0]:
                    result.append([x,-height_till_uninclusive_heap[0][0]])
            else: # right of the building
                curr_height = - height_till_uninclusive_heap[0][0] if height_till_uninclusive_heap else 0
                # current building's right is not dup with some building's left and height != previous height
                if x != result[-1][0] and result[-1][1] != curr_height:
                    result.append([x, curr_height])

        return result

if __name__ =='__main__':
    s = Solution()
    assert [[1,219],[2,228],[19,225],[45,229],[89,190],[95,175],[97,152],[99,74],[100,0]] == \
           s.getSkyline([[1,38,219],[2,19,228],[2,64,106],[3,80,65],[3,84,8],[4,12,8],[4,25,14],[4,46,225],[4,67,187],[5,36,118],[5,48,211],[5,55,97],[6,42,92],[6,56,188],[7,37,42],[7,49,78],[7,84,163],[8,44,212],[9,42,125],[9,85,200],[9,100,74],[10,13,58],[11,30,179],[12,32,215],[12,33,161],[12,61,198],[13,38,48],[13,65,222],[14,22,1],[15,70,222],[16,19,196],[16,24,142],[16,25,176],[16,57,114],[18,45,1],[19,79,149],[20,33,53],[21,29,41],[23,77,43],[24,41,75],[24,94,20],[27,63,2],[31,69,58],[31,88,123],[31,88,146],[33,61,27],[35,62,190],[35,81,116],[37,97,81],[38,78,99],[39,51,125],[39,98,144],[40,95,4],[45,89,229],[47,49,10],[47,99,152],[48,67,69],[48,72,1],[49,73,204],[49,77,117],[50,61,174],[50,76,147],[52,64,4],[52,89,84],[54,70,201],[57,76,47],[58,61,215],[58,98,57],[61,95,190],[66,71,34],[66,99,53],[67,74,9],[68,97,175],[70,88,131],[74,77,155],[74,99,145],[76,88,26],[82,87,40],[83,84,132],[88,99,99]])

# @lc code=end

