#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

"""

# Leet Code Solution

def solution(priorities, location):
    process = [ [priorities[i], i] for i in range(len(priorities))]
    sortedData = sorted(process, key=lambda x: x[0], reverse=True)

    executeTime = 0
    while len(process) > 0:
        current = process.pop(0)
        if current[0] == sortedData[0][0]:
            executeTime += 1
            sortedData.pop(0)
            if current[1] == location:
                return executeTime
            continue
        process.append(current)

    return executeTime



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
        res = solution([2, 1, 3, 2], 2)
        self.assertEqual(res, 1)

    def test_case_2(self):
        res = solution([1, 1, 9, 1, 1, 1], 0)
        self.assertEqual(res, 5)




if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
