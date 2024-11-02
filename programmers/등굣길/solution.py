#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

I o o o
o x o o
o o o O

I 1 1 x
1 2 3 3
x 2 5 8

I 1 1 1
1 x 1 2
1 1 2 4

I 1 1 1
1 2 x 1
1 3 3 4

I 1 x o
x 1 1 1
o 1 2 3

"""

# Leet Code Solution

def solution(m, n, puddles) -> int:
    # 한길이면 무조건 1
    if n == 1 or m == 1:
        return 1

    # 지도 좌표 생성
    navigate = [[0] * m for _ in range(n)]
    # 장애물 위치 설정
    for x, y in puddles:
        navigate[y - 1][x - 1] = -1

    # 시작 최단거리 좌표 설정
    for i in range(m):
        if navigate[0][i] == -1:
            for j in range(i, m):
                navigate[0][j] = -1
            break
        navigate[0][i] = 1
    for i in range(n):
        if navigate[i][0] == -1:
            for j in range(i, n):
                navigate[j][0] = -1
            break
        navigate[i][0] = 1

    # 나머지 최단거리 계산
    for y in range(1, n):
        for x in range(1, m):
            # 장애물이면 무시
            if navigate[y][x] == -1:
                continue
            agoy = navigate[y - 1][x]
            agox = navigate[y][x - 1]
            if agoy == -1:
                navigate[y][x] = agox
                continue
            if agox == -1:
                navigate[y][x] = agoy
                continue
            navigate[y][x] = (agoy + agox) % 1000000007

    # for navi in navigate:
    #     print(navi)

    answer = navigate[n - 1][m - 1]
    if answer == -1:
        return 0
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
        res = solution(4, 3, [[2, 2]])
        self.assertEqual(res, 4)



if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
