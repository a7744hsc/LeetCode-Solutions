#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False

        i = 0
        while i < len(data):
            if data[i] >> 7 == 0:
                i += 1
            elif data[i] >> 5 == 0b110:
                if i + 1 >= len(data):
                    return False
                if data[i + 1] >> 6 != 0b10:
                    return False
                i += 2
            elif data[i] >> 4 == 0b1110:
                if i + 2 >= len(data):
                    return False
                if data[i + 1] >> 6 != 0b10:
                    return False
                if data[i + 2] >> 6 != 0b10:
                    return False
                i += 3
            elif data[i] >> 3 == 0b11110:
                if i + 3 >= len(data):
                    return False
                if data[i + 1] >> 6 != 0b10:
                    return False
                if data[i + 2] >> 6 != 0b10:
                    return False
                if data[i + 3] >> 6 != 0b10:
                    return False
                i += 4
            else:
                return False
        return True
        


# @lc code=end
