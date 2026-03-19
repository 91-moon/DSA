# Leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        row = len(heights)
        col = len(heights[0])

        def dfs(i, j, ocn):

            for x, y in direction:
                nx = i + x
                ny = j + y
                if 0 <= nx < row and 0 <= ny < col and heights[i][j] <= heights[nx][ny] and (nx, ny) not in ocn:
                    ocn.add((nx, ny))
                    dfs(nx, ny, ocn)

        pac = set()
        atl = set()
        for i in range(row):
            pac.add((i, 0))
            dfs(i, 0, pac)
            atl.add((i, col - 1))
            dfs(i, col - 1, atl)

        for i in range(col):
            pac.add((0, i))
            dfs(0, i, pac)
            atl.add((row - 1, i))
            dfs(row - 1, i, atl)
        final = atl & pac

        return [list(item) for item in final]