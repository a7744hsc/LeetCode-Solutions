from typing import List,Dict


class Solution:
    def permute(self,nums):
        result = []
        if not nums:
            return result

        i=0
        current_candidates=[[]]
        while i< len(nums):
            new_candidates=[]
            for cand in current_candidates:
                for j in range(len(cand)+1):
                    cand_c = cand.copy()
                    cand_c.insert(j, nums[i])
                    new_candidates.append(cand_c)
            current_candidates = new_candidates
            i+=1

        return current_candidates


if __name__ == '__main__':
    test_cases = [(([0,1],),[[0,1],[1,0]])
    ]
    s = Solution()
    for i,o in test_cases:
        out = s.permute(*i)
        for array in out:
            assert any([array == o_array for o_array in o])
        assert len(o) == len(out), f'failed on test case test case {i},{o},{s.permute(*i)}'

    print('All case passed')