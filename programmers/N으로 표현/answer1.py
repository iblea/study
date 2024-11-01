#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


# https://kom-story.tistory.com/259

def solution(N, number):

    answer = 9
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        # 연산자 몇번 사용할지 획득
        for cnt in range(1, i):
            # 최종적으로 N을 i번 사용해서 만들 수 있는 수들을 획득해야 함.
            # 그러기 위해서는 N을 cnt번 사용해서 만들 수 있는 수와 N을 i-cnt번 사용해서 만들 수 있는 수를 연산해야 함.
            # i = 6, cnt = 1, i - cnt = 5
            # 첫 번째 숫자를 획득
            # N을 cnt번 사용해서 만들 수 있는 모든 수 획득
            for a in dp[cnt]:
                # N을
                for b in dp[i - cnt]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            return i

    return -1



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
        res = solution(5,12)
        self.assertEqual(res, 4)

    def test_case_2(self):
        res = solution(2,11)
        self.assertEqual(res, 3)

    def test_case_3(self):
        res = solution(1,11111)
        self.assertEqual(res, 5)

    def test_case_4(self):
        res = solution(1,999999)
        self.assertEqual(res,-1)

    def test_case_5(self):
        res = solution(5,500)
        self.assertEqual(res,5)

    def test_case_6(self):
        res = solution(5,30525)
        self.assertEqual(res,5)

    def test_case_7(self):
        res = solution(9,81)
        self.assertEqual(res,2)

    def test_case_8(self):
        res = solution(5,3025)
        self.assertEqual(res,4)

    def test_case_9(self):
        res = solution(9,0)
        self.assertEqual(res,2)


    def test_case_10(self):
        res = solution(1, 1121)
        self.assertEqual(res,7)

    def test_case_11(self):
        # 4 * 4 + 4 / 4
        res = solution(4, 17)
        self.assertEqual(res,4)







if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)

