from typing import List,Dict


class Solution:
    def longestIncreasingPath(self,matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        longest_path_for_each_point_as_start = [[-1]*col_len for _ in range(row_len)]

        def find_longest_path_for(x,y):
            if longest_path_for_each_point_as_start[x][y] != -1:
                return longest_path_for_each_point_as_start[x][y]
            length_candidate = [1]
            current_value = matrix[x][y]
            if x-1>=0 and current_value< matrix[x-1][y]:
                length_candidate.append(1+ find_longest_path_for(x-1,y))
            if x + 1 < row_len and current_value < matrix[x + 1][y]:
                length_candidate.append(1 + find_longest_path_for(x + 1, y))
            if y-1 >=0 and current_value < matrix[x][y - 1]:
                length_candidate.append(1 + find_longest_path_for(x, y - 1))
            if y+1 < col_len and current_value < matrix[x][y + 1]:
                length_candidate.append(1 + find_longest_path_for(x, y + 1))
            longest_path_for_each_point_as_start[x][y] = max(length_candidate)
            return longest_path_for_each_point_as_start[x][y]
        for i in range(row_len):
            for j in range(col_len):
                find_longest_path_for(i,j)
        return max([max(line) for line in longest_path_for_each_point_as_start])



if __name__ == '__main__':
    test_cases = [(([[9,9,4],[6,6,8],[2,1,1]],),4)
    ]
    s = Solution()
    for i,o in test_cases:
        result = s.longestIncreasingPath(*i)
        assert o == result, f'failed on test case test case {i},{o},{result}'

    print('All case passed')