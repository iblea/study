# !/usr/bin/python3
import unittest
from typing import List
from random import randint
from copy import deepcopy


"""
Solution Note

matrix[n][n]
n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9 ( 1billion )
1 <= k <= n * n

All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
"""

def merge_sort(arr, n):
    merge = arr
    for i in range(1, n+1, 2): # i: 분할할 크기
        if i!= 1:
            i -= 1
        si = 0  # 인덱스
        while si < n:
            # 분할 범위 단위로 정렬
            index1 = si
            index2 = si+i
            m = []
            # index2가 배열 길이를 초과했을 경우(index1+i이 배열 끝일 경우)
            if index2 >= n:
                index2 = si

            # index 1 >= 분할크기 또는 index 2 >= 분할크기*2 일때
            while index1-si < i or index2-si < i * 2:
                if index2 == si:
                    m = merge[si:]
                    break
                if index1-si >= i:
                    if index2 >= n:
                        break
                    m.append(merge[index2])
                    index2+=1
                    continue
                elif index2-si-i >= i or index2 >= n:
                    m.append(merge[index1])
                    index1+=1
                    continue
                if int(merge[index1]) < int(merge[index2]):
                    m.append(merge[index1])
                    index1+=1
                else:
                    m.append(merge[index2])
                    index2+=1
            merge = merge[:si] + m + merge[si+(i*2):]
            si += i*2
    return merge


def pnt_array(arr2d):
    for arr in arr2d:
        print("[ ", end="")
        for i in arr:
            print("{:02d}".format(i), end=", ")
        print("\b\b ]")
    print("")

def make_array(arrlen, pnt_option = False):
    input_data = []
    for i in range(arrlen):
        tmp = []
        for j in range(arrlen):
            tmp.append(randint(1, 99))
        input_data.append(deepcopy(tmp))

    if pnt_option is True:
        pnt_array(input_data)
    return input_data


def make_answer_2d(answer, arr_sqr_len):
    answer_2d = []
    tmp = []
    for i in range(len(answer)):
        tmp.append(answer[i])
        if (i + 1) % arr_sqr_len == 0:
            answer_2d.append(deepcopy(tmp))
            tmp = []
    return answer_2d

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

    def test_case_normal(self):
        ago_arr = [7,6,4,5,2,3,1]
        after_arr = merge_sort(ago_arr, len(ago_arr))
        answer = [1, 2, 3, 4, 5, 6, 7]
        self.assertEquals(after_arr, answer)

        # self.assertEquals(answer_2d, matrix)




if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
    pass
