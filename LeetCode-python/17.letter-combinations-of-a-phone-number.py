#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from unicodedata import digit
from webbrowser import get


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map= {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if not digits:
            return []
        def get_combinations(digits,prefix):
            if len(digits)==1:
                return[prefix+c for c in map[digits]]
            else:
                result = []
                for c in map[digits[0]]:
                    result+= get_combinations(digits[1:],prefix+c)
                return result
        return get_combinations(digits,'')
# @lc code=end

