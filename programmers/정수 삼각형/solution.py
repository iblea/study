#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5

       7
    10   15
   18  16  15
 20  25  20  19
 2 7 4 4
4 5 2 6 5

->
8
10, 15
18, 11, 16, 15

7 + 3 + 8 + 2 [0] [0]
7 + 3 + 8 + 7 [0] [1]
7 + 3 + 1 + 7 [1] [1]
7 + 3 + 1 + 4 [1] [2]
7 + 8 + 1 + 7 [2] [2]
7 + 8 + 1 + 4 [2] [3]
7 + 8 + 0 + 4 [3] [3]
7 + 8 + 0 + 4 [3] [4]

7 + 3 + 8 + 2 + 4 [0][0]
7 + 3 + 8 + 2 + 5 [0][1]
7 + 3 + 8 + 7 + 5 [1][1]
7 + 3 + 8 + 7 + 2 [1][2]
7 + 3 + 1 + 7 + 5 [2][1]
7 + 3 + 1 + 7 + 2 [2][2]

?? 그러고보니 이렇게 해야하나?
이중에서 제일 큰 값만 기억하면 되잖아!!
"""

# Leet Code Solution

def my_solution(triangle) -> int:
    dp = [ [] for _ in range(len(triangle)) ]
    dp[0] += [(triangle[0][0], 0)]
    trianglelen = len(triangle)
    if trianglelen == 1:
        return dp[0][0][0]

    for i in range(1, trianglelen):
        line = triangle[i]
        ago_sumarr = dp[i-1]
        for j in range(len(ago_sumarr)):
            agotuple = ago_sumarr[j]
            agonum = agotuple[0]
            agoidx = agotuple[1]
            dp[i].append((agonum + line[agoidx], agoidx))
            dp[i].append((agonum + line[agoidx+1], agoidx+1))

    arr = dp[-1]
    return max(arr, key=lambda x: x[0])[0]


def solution(triangle) -> int:
    dp = [ [] for _ in range(len(triangle)) ]
    dp[0] += [ triangle[0][0] ]
    trianglelen = len(triangle)
    if trianglelen == 1:
        return dp[0][0]

    # print(dp)
    for i in range(1, trianglelen):
        line = triangle[i]
        agodp = dp[i-1]
        dp[i].append(agodp[0] + line[0])
        for j in range(1, len(agodp)):
            nextnum = max(agodp[j-1], agodp[j])
            dp[i].append(nextnum + line[j])
        dp[i].append(agodp[-1] + line[-1])
        # print(dp)

    arr = dp[-1]
    # print(arr)
    return max(arr)


# python unit test
class UnitTest(unittest.TestCase):

    # 클래스 생성 시 1회 실행
    @classmethod
    def setUpClass(self):
        pass

    # 클래스 소멸 시 1회 실행
    @classmethod
    def tearDownClass(self):
        pass

    # 테스트 케이스 전 실행
    def setUp(self):
        pass

    # 테스트 케이스 후 실행
    def tearDown(self):
        pass

    def test_case_1(self):
        res = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
        self.assertEqual(res, 30)



if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
