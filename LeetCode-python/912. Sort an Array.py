from typing import List,Dict
import random

class Solution: #quick sort
    def sortArray(self, nums,start=None,end=None):
        #return sorted(nums)

        if start is None or end is None:
            start=0
            end=len(nums)
        if end - start <= 1:
            return nums

        a_i = random.randint(start,end-1)
        nums[end-1],nums[a_i] = nums[a_i],nums[end-1]
        anchor = nums[end-1]
        left = start
        right =end-1
        while left < right:
            while nums[left]<=anchor and left<right:
                left+=1

            if left<right:
                nums[right] = nums[left]
                right-=1

            while nums[right]>= anchor and left<right:
                right-=1

            if left<right:
                nums[left] = nums[right]
                left+=1
        assert left == right
        nums[left] = anchor

        self.sortArray(nums,start,left)
        self.sortArray(nums,left+1,end)
        return nums


if __name__ == '__main__':
    test_cases = [([5,1,1,2,0,0],[0,0,1,1,2,5])
    ]
    s = Solution()
    for i,o in test_cases:
        result = s.sortArray(i)
        assert o == result, f'failed on test case test case {i},{o},{result}'

    print('All case passed')