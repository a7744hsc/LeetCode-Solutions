from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev = nums[0]
        max_len = 1
        current_len = 1
        for n in nums[1:]:
            if n>prev:
                current_len+=1
                prev = n
            else:
                max_len = current_len if current_len > max_len else max_len
                current_len=1
                prev=n
        if current_len > max_len:
            max_len = current_len

        return max_len


if __name__ == '__main__':
    test_cases = [([1,3,5,4,7],3),([2,2,2,2,2],1)]
    s = Solution()
    for i,o in test_cases:
        assert o == s.findLengthOfLCIS(i), f'failed on test case test case {i},{o}'

    print('All case passed')