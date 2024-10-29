#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

"""

# Leet Code Solution

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_str: str = bin(arr1[i] | arr2[i])[2:].zfill(n)
        sharp_str = bin_str.replace('1', '#').replace('0', ' ')
        answer.append(sharp_str)
    return answer



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
        res = solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28])
        self.assertEqual(res, ["#####", "# # #", "### #", "#  ##", "#####"])

    def test_case_2(self):
        res = solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
        self.assertEqual(res, ["######", "###  #", "##  ##", " #### ", " #####", "### # "]);



if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
