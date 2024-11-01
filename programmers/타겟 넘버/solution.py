#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

"""

# Leet Code Solution

def solution(numbers, target):
    def dfs(idx, sum):
        if idx == len(numbers):
            if sum == target:
                return 1
            return 0

        d1 = dfs(idx + 1, sum + numbers[idx])
        d2 = dfs(idx + 1, sum - numbers[idx])
        return d1 + d2

    return dfs(0, 0)



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
        res = solution([1,1,1,1,1], 3)
        self.assertEqual(res, 5)

    def test_case_2(self):
        res = solution([4,1,2,1], 4)
        self.assertEqual(res, 2)



if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
