#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

"""

# Leet Code Solution

def solution(begin, target, words):

    def func(b, arr, cnt):
        global answer
        if b == target:
            return cnt

        ret = 0
        for i in range(len(arr)):
            word = arr[i]
            res = diff_word(b, word)
            if res is False:
                continue
            c = func(word, arr[:i] + arr[i+1:], cnt+1)
            if c != 0:
                if ret == 0:
                    ret = c
                else:
                    ret = min(ret, c)
        return ret

    return func(begin, words, 0)


def diff_word(word1: str, word2: str) -> bool:
    wordlen = len(word1) + 1
    for i in range(0, wordlen):
        w1 = word1[:i] + word1[i+1:]
        w2 = word2[:i] + word2[i+1:]
        if w1 == w2:
            return True
    return False


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
        res = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        self.assertEqual(res, 4)

    def test_case_2(self):
        res = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        self.assertEqual(res, 0)



if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
