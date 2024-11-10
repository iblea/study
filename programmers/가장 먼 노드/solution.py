#!/usr/bin/python3
import unittest
from typing import List
from typing import Optional


"""
Solution Note

"""

# Leet Code Solution

def solution(n, edge):
    answer = 0
    # dict
    edges = [ [] for i in range(n + 1)]
    visited = [ -1 for i in range(n + 1)]
    for i in range(1, n + 1):
        edges[i] = []
    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])

    visited[1] = 0
    que = [(1, 0)]
    while que:
        node, depth = que.pop(0)
        depth += 1
        for n in edges[node]:
            if visited[n] == -1 or visited[n] > depth:
                visited[n] = depth
                que.append((n, depth))

    max_depth = max(visited)
    for v in visited:
        if v == max_depth:
            answer += 1
    return answer


def solution_recursive(n, edge):
    answer = 0
    # dict
    edges = [ [] for i in range(n + 1)]
    visited = [ -1 for i in range(n + 1)]
    for i in range(1, n + 1):
        edges[i] = []
    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])

    def dfs(start, depth):
        nonlocal visited
        depth += 1
        for node in edges[start]:
            if visited[node] == -1 or visited[node] > depth:
                visited[node] = depth
                dfs(node, depth)
    visited[1] = 0
    dfs(1, 0)
    max_depth = max(visited)
    for v in visited:
        if v == max_depth:
            answer += 1
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
        res = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
        self.assertEqual(res, 3)

    def test_case_2(self):
        res = solution(2, [[1, 2]])
        self.assertEqual(res, 1)



if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
