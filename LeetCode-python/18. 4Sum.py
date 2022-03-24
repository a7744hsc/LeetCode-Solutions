from typing import List,Dict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        result = set()
        for i in range(length):
            if nums[i] + sum(nums[-3:]) < target:
                continue
            for j in range(i + 1, length):
                if nums[i] + nums[j] + sum(nums[-2:]) < target:
                    continue
                p = j + 1
                q = length - 1
                while p < q:
                    if nums[i] + nums[j] + nums[p] + nums[q] == target:
                        result.add((nums[i], nums[j], nums[p], nums[q]))
                        p += 1
                        q -= 1
                    elif nums[i] + nums[j] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        q -= 1

        return [list(t) for t in result]


if __name__ == '__main__':
    test_cases = [([[1,0,-1,0,-2,2], 0],[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
    ]
    s = Solution()
    for i,o in test_cases:
        assert o == s.fourSum(*i), f'failed on test case test case {i},{o}'

    print('All case passed')