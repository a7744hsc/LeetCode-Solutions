from typing import List,Dict


class Solution:
    def maxSubArray(self,nums):
        max_sum = []
        for digit in nums:
            if not max_sum:
                max_sum.append(digit)
            else:
                max_sum.append(max(max_sum[-1]+digit,digit))
        return max(max_sum)


if __name__ == '__main__':
    test_cases = [(([-2,1,-3,4,-1,2,1,-5,4],),6)
    ]
    s = Solution()
    for i,o in test_cases:
        result = s.maxSubArray(*i)
        assert o == result, f'failed on test case test case {i},{o},{result}'

    print('All case passed')