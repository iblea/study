# https://www.acmicpc.net/problem/2798

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
        "input2.txt",
    ]

    for testfile in testfiles:
        if inputFile(testfile) is True:
            main()



def main() -> None:
    cardsLen, limit = map(int, input().split())
    cards = list(map(int, input().split()))

    result = 0
    for i in range(0, cardsLen - 2):
        for j in range(i + 1, cardsLen - 1):
            for k in range(j + 1, cardsLen):
                num3_sum: int = cards[i] + cards[j] + cards[k]
                if num3_sum > limit:
                    continue
                if num3_sum > result:
                    result = num3_sum

    print(result)



if __name__ == "__main__":
    # main()

    test()
