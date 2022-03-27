from typing import List,Dict
from collections import deque

class Solution:
    def isMatch(self,s,p):
        d = {}
        p_list =  p.split()
        new_p = ''
        for p_char in p_list:
            if p_char =='*' and new_p and new_p[-1] =='*':
                continue
            new_p+=p_char

        return self.isMatch_(s,new_p,d)

    def isMatch_(self,s,p,cache):
        if (len(s),len(p)) in cache:
            return cache[(len(s),len(p))]
        if len(s)>0 and len(p)==0:
            cache[(len(s), len(p))] =False
            return False
        if len(s)==0 and len(p)==0:
            cache[(len(s), len(p))] = True
            return True
        if len(s)==0 and len(p)>0:
            if all([p_char =='*' for p_char in p]):
                cache[(len(s), len(p))] = True
                return True
            else:
                cache[(len(s), len(p))] = False
                return False

        if p[0] == '?' :
            cache[(len(s), len(p))] = self.isMatch_(s[1:],p[1:],cache)
        elif p[0] == '*':
            # cache[(len(s), len(p))] = any([self.isMatch_(s[i:],p[1:],cache) for i in range(len(s)+1)])
            cache[(len(s), len(p))] = self.isMatch_(s,p[1:],cache) or self.isMatch_(s[1:], p, cache)
        elif s[0] == p[0]:
            cache[(len(s), len(p))] = self.isMatch_(s[1:],p[1:],cache)
        else:
            cache[(len(s), len(p))] = False

        return cache[(len(s), len(p))]


class Solution1:
    def isMatch(self,s,p):
        d = {}
        p_list =  p.split()
        new_p = ''
        for p_char in p_list:
            if p_char =='*' and new_p and new_p[-1] =='*':
                continue
            new_p+=p_char

        return self.isMatch_(s,new_p,d)

    def isMatch_(self,s,p,cache):
        if (len(s),len(p)) in cache:
            return cache[(len(s),len(p))]
        if len(s)>0 and len(p)==0:
            cache[(len(s), len(p))] =False
            return False
        if len(s)==0 and len(p)==0:
            cache[(len(s), len(p))] = True
            return True
        if len(s)==0 and len(p)>0:
            if all([p_char =='*' for p_char in p]):
                cache[(len(s), len(p))] = True
                return True
            else:
                cache[(len(s), len(p))] = False
                return False

        if p[0] == '?':
            cache[(len(s), len(p))] = self.isMatch_(s[1:],p[1:],cache)
        elif p[0] == '*':
            cache[(len(s), len(p))] = any([self.isMatch_(s[i:],p[1:],cache) for i in range(len(s),-1,-1)])
            # cache[(len(s), len(p))] = self.isMatch_(s,p[1:],cache) or self.isMatch_(s[1:], p, cache)
        elif s[0] == p[0]:
            cache[(len(s), len(p))] = self.isMatch_(s[1:],p[1:],cache)
        else:
            cache[(len(s), len(p))] = False

        return cache[(len(s), len(p))]

if __name__ == '__main__':
    test_cases = [(("aa", "a"),False),
                  (("aa", "*"),True),
                  (("cb", "?a"),False),
                  (("bbaabbbbaaaabaabbbbabababaabaaaabaaabbaabaabaaabbabaabbbbbbbbbbaababbabaabbabaababbaaaabbbbaaaaaababbbbabbaababbabbabbababbbbabbbbaabaaabbaababbbaaaaababbbabbaaaaababbbaabbaabbbbbbbbbaababaababbababbabaa","*b****abb***bbba**b*baaa****ba*ab***a*ab**a*a***aabbabb*bb**b***bbbbab****b*ba*baa*b*aa*b*b***a*bbab*"),False)
    ]
    s = Solution()
    for i,o in test_cases:
        result = s.isMatch(*i)
        assert o == result, f'failed on test case test case {i},{o},{result}'

    print('All case passed')

    i,o = test_cases[-1]
    import timeit
    time1 = timeit.timeit(lambda:s.isMatch(*i),number=10)
    print(time1)
    s1= Solution1()
    time2 = timeit.timeit(lambda: s1.isMatch(*i),number=10)
    print(time2)