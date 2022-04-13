#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
from typing import List


class Solution:
    @staticmethod
    def is_1_on_bit(x,num):
        return bool((1<<(x-1)) & num)

    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return False
        i = 0
        while i <len(data):
            num = data[i]
            if not Solution.is_1_on_bit(8,num):
                i+=1
                continue
            else:
                leading_1 = 1
            if Solution.is_1_on_bit(7,num):
                leading_1+=1
                if Solution.is_1_on_bit(6,num):
                    leading_1+=1
                    if Solution.is_1_on_bit(5,num):
                        leading_1+=1
                        if Solution.is_1_on_bit(4,num):
                            leading_1+=1
            
            if leading_1 == 5 or leading_1 == 1:
                return False
            if leading_1 == 2:
                if i+1>=len(data):
                    return False
                else:
                    if Solution.is_1_on_bit(8,data[i+1]) and not Solution.is_1_on_bit(7,data[i+1]):
                        i+=2
                        continue
                    else:
                        return False
            
            if leading_1 == 3:
                if i+2>=len(data):
                    return False
                else:
                    if Solution.is_1_on_bit(8,data[i+1]) and not Solution.is_1_on_bit(7,data[i+1])\
                        and Solution.is_1_on_bit(8,data[i+2]) and not Solution.is_1_on_bit(7,data[i+2]):
                         i+=3
                         continue
                    else:
                        return False
            
            if leading_1 == 4:
                if i+3>=len(data):
                    return False
                else:
                    if Solution.is_1_on_bit(8,data[i+1]) and not Solution.is_1_on_bit(7,data[i+1])\
                        and Solution.is_1_on_bit(8,data[i+2]) and not Solution.is_1_on_bit(7,data[i+2])\
                        and Solution.is_1_on_bit(8,data[i+3]) and not Solution.is_1_on_bit(7,data[i+3]):
                         i+=4
                         continue
                    else:
                        return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([234,130,130]))
# @lc code=end
