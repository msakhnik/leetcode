import unittest
from typing import List, Iterator
from collections import defaultdict


def bfs(graph: dict, start: str, end: str) -> Iterator[List]:
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for _next in graph[vertex] - set(path):
            if _next == end:
                yield path + [_next]
            else:
                queue.append((_next, path + [_next]))


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        graph = defaultdict(set)
        start = end = None
        blocks = list()
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                key = "{}{}".format(i, j)
                if item == 1:
                    start = key
                elif item == 2:
                    end = key
                elif item == -1:
                    blocks.append(key)
                    continue
                if i:
                    p_key = "{}{}".format(i - 1, j)
                    if p_key not in blocks:
                        graph[p_key].add(key)
                        graph[key].add(p_key)
                if j:
                    p_key = "{}{}".format(i, j - 1)
                    if p_key not in blocks:
                        graph[p_key].add(key)
                        graph[key].add(p_key)
        pathes = bfs(graph, start, end)
        counter = 0
        for sub in pathes:
            if len(sub) == len(graph):
                counter += 1
        return counter


class TestUniquePathIII(unittest.TestCase):
    def test_example1(self):
        data = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
        sol = Solution()
        self.assertEqual(sol.uniquePathsIII(data), 2)

    def test_example2(self):
        data = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
        sol = Solution()
        self.assertEqual(sol.uniquePathsIII(data), 4)

    def test_example3(self):
        data = [[0, 1], [2, 0]]
        sol = Solution()
        self.assertEqual(sol.uniquePathsIII(data), 0)


unittest.main()
