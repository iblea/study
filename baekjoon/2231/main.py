# https://www.acmicpc.net/problem/2231

import os
import sys

# https://daebaq27.tistory.com/57

def inputFile(filename) -> bool:
    if os.path.isfile(filename) is False:
        print("[{}] 파일이 존재하지 않습니다.".format(filename))
        return False
    sys.stdin = open(filename, "rt")
    # n,m = map(int, input().split())
    # # arr = [list(map(int, input().split())) for _ in range(m)]
    # arr = list(map(int, input().split()))
    return True


def test() -> None:

    testfiles : list[str] = [
        "input1.txt",
    ]

    for testfile in testfiles:
        if inputFile(testfile) is True:
            main()



def main() -> None:
    # number = map(int, input().split())
    number = int(input())

    print(baekjoon(number))

def addDight(num) -> int:
    _sum: int = 0
    while (num > 0):
        _sum += num % 10
        num //= 10
    return _sum

def baekjoon(number) -> int:
    if number < 2:
        return 0

    # 성능을 위해 절반 지점까지만 검사
    breaker: int = number // 2 - 1;
    result = 0
    for num in range(number - 1, breaker, -1):
        if num + addDight(num) == number:
            result = num

    return result

if __name__ == "__main__":
    main()

    # test()


def baekjoon1(number) -> int:
    for i in range(1, number+1):   # 해당 분해합의 생성자 찾기
        num: int = sum((map(int, str(i))))  # i의 각 자릿수를 더함
        # print (num)
        num_sum: int = i + num  # 분해합 = 생성자 + 각 자릿수의 합
        # print(num_sum, i, num, number)
        # print("")
        if num_sum == number:
            return i
    return 0



