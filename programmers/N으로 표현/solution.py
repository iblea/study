#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
입출력 예
N	number	return
5	12	4
2	11	3
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.


5->1
0: 5

5->2
0: 55,
1: 5+5, 5-5, 5*5, 5/5

5->3
0: 555
1: (55)+5, (55)-5, (55)*5, (55)/5
2: (5+5)+5, (5+5)-5, (5+5)*5, (5+5)/5, (5-5)+5, (5-5)-5, (5-5)*5, (5-5)/5, (5*5)+5, (5*5)-5, (5*5)*5, (5*5)/5, (5/5)+5, (5/5)-5, (5/5)*5, (5/5)/5

5->4
0: 5555
1: (555)+5, (555)-5, (555)*5, (555)/5, (55+55), (55-55), (55*55), (55/55)
2: (55+5)+5, (55+5)-5, (55+5)*5, (55+5)/5, (55-5)+5, (55-5)-5, (55-5)*5, (55-5)/5, (55*5)+5, (55*5)-5, (55*5)*5, (55*5)/5, (55/5)+5, (55/5)-5, (55/5)*5, (55/5)/5
3: 5+5+5+5, 5+5+5-5, ... 5/5/5/5, 5*5+5/5

5->5:
0: 55555
1: (5555)+5, (5555)-5, (5555)*5, (5555)/5, (555+55), (555-55), (555*55)
4, 1, 3, 2
...

5->6
0: 555555
1: (55555)+5, (55555)-5, (55555)*5, (55555)/5, (5555+55), (5555-55), (5555*55), (5555/55), (555+555), (555-555), (555*555), (555/555)
- 5, 1 |
2: (5555+5)+5, (5555+5)-5, (5555+5)*5, (5555+5)/5, (5555-5)+5, (5555-5)-5, (5555-5)*5, (5555-5)/5, (5555*5)+5, (5555*5)-5, (5555*5)*5, (5555*5)/5, (5555/5)+5, (5555/5)-5, (5555/5)*5, (5555/5)/5, (555+55)+5, (555+55)-5, (555+55)*5, (555+55)/5, (555-55)+5, (555-55)-5, (555-55)*5, (555-55)/5, (555*55)+5, (555*55)-5, (555*55)*5, (555*55)/5, (555/55)+5, (555/55)-5, (555/55)*5, (555/55)/5
- 4, 1, 1 | 3, 2, 1
-
...

"""

# Leet Code Solution


def solution(N, number):

    for i in range(1, 9):
        for oper_cnt in range(0, i):
            # 연산할 숫자들의 자릿수 배열을 생성한다.
            # 만약 숫자 6개, 연산자 1개를 사용해 표현할 경우
            # 55555 ? 5, 5555 ? 55, 555 ? 555 -> [[5,1], [4,2], [3,3]] 으로 표현할 수 있다.

            numarray = get_numbers_array(i, oper_cnt)

            nums = []
            for arr in numarray:
                tmp = []
                for j in arr:
                    tmp.append(getnum(j, N))
                nums.append(tmp)

            for j in range(len(nums)):
                if oper(nums[j], number) is True:
                    return i

    # if answer > 8:
    #     answer = -1
    return -1

def get_numbers_array(numcount, opercount):
    # numcount = 6, opercount = 0 -> [[6]]
    # numcount = 6, opercount = 1 -> [[5,1], [4,2], [3,3]]
    # numcount = 6, opercount = 2 -> [[4,1,1], [3,2,1], [2,2,2]]
    # numcount = 5, opercount = 0 -> [[5]]
    # numcount = 5, opercount = 1 -> [[4,1], [3,2]]
    # numcount = 5, opercount = 2 -> [[3,1,1], [2,2,1], [2,1,2]]
    # numcount = 5, opercount = 3 -> [[2,1,1,1]]
    arraylen = opercount + 1
    if opercount == 0:
        return [[numcount]]

    result = []

    def func(val, cnt, l):
        maxval = val-cnt + 1
        suml = sum(l)
        lenl = len(l)
        lastindex = maxval
        if lenl >= 1:
            lastindex = l[lenl-1]

        for i in range(maxval, 0, -1):
            if lastindex < i:
                continue
            if cnt == 1:
                if suml + i == numcount:
                    result.append(l + [i])
                continue
            func(val-i, cnt-1, l+[i])

    func(numcount, arraylen, [])
    return result


def getnum(c, N):
    if c == 0:
        return 0

    if c == 1:
        return N

    strN = str(N)
    return int(''.join([ strN for _ in range(c) ]))


def oper(numlist, expected):
    if len(numlist) == 0:
        return False

    def func(remains):
        if len(remains) == 1:
            if remains[0] == expected:
                return True
            return False
        traversal = len(remains) - 1


        # 성능 개선하기 위해 +와 *는 자릿수 기반 연산을 배제한다.
        arr = [ remains[0] + remains[1] ] + remains[2:]
        if func(arr) is True:
            return True
        arr = [ remains[0] * remains[1] ] + remains[2:]
        if func(arr) is True:
            return True

        for i in range(traversal):
            minus= remains[i] - remains[i+1]
            arr = remains[:i] + [ minus ] + remains[i+2:]
            if func(arr) is True:
                return True
            if remains[i+1] == 0:
                return False
            arr = remains[:i] + [ remains[i] // remains[i+1] ] + remains[i+2:]
            if func(arr) is True:
                return True
        return False

    return func(numlist)



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
