from main import baekjoon, baekjoon1

import unittest

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
        res: int = baekjoon1(10)
        self.assertEqual(res, 5)

    def test_case_2(self):
        res: int = baekjoon(216)
        self.assertEqual(res, 198)

    def test_case_3(self):
        res: int = baekjoon(9)
        self.assertEqual(res, 0)

    def test_case_4(self):
        res: int = baekjoon(1)
        self.assertEqual(res, 0)

    def test_case_5(self):
        res: int = baekjoon(1000000)
        self.assertEqual(res, 0)

    def test_case_6(self):
        res: int = baekjoon(13)
        self.assertEqual(res, 11)

    def test_case_7(self):
        res: int = baekjoon(11)
        self.assertEqual(res, 10)

    # 예외케이스 생각 못함.
    def test_case_8(self):
        res: int = baekjoon1(2)
        self.assertEqual(res, 1)

    def test_case_answer(self):
        for i in range(1, 1000001):
            # print(i)
            res: int = baekjoon(i)
            answer = baekjoon1(i)
            self.assertEqual(res, answer)




if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
    pass
