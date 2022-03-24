from typing import List,Dict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lts_with_last_digit_for_each_position = [1]*len(nums)
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums[:i]):
                if num1>num2:
                    lts_with_last_digit_for_each_position[i] = max(lts_with_last_digit_for_each_position[i],lts_with_last_digit_for_each_position[j]+1)
        return  max(lts_with_last_digit_for_each_position)


if __name__ == '__main__':
    test_cases = [([10,9,2,5,3,7,101,18],4),
                  ([0,1,0,3,2,3],4),
                  ([7,7,7,7,7,7,7],1)
    ]
    s = Solution()
    for i,o in test_cases:
        assert o == s.lengthOfLIS(i), f'failed on test case test case {i},{o}'

    print('All case passed')