class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = ((-1,0),(0,-1))
        res = [[0]*n for _ in range(m)]
        res[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                pos = (i,j)
                next_pos_0 = (pos[0]+moves[0][0], pos[1]+moves[0][1])
                next_pos_1 = (pos[0]+moves[1][0], pos[1]+moves[1][1])
                print(next_pos_0, next_pos_1)
                if 0 <= next_pos_0[0] < m and 0 <= next_pos_0[1] < n:
                    res[i][j] += res[next_pos_0[0]][next_pos_0[1]]
                if 0 <= next_pos_1[0] < m and 0 <= next_pos_1[1] < n:
                    res[i][j] += res[next_pos_1[0]][next_pos_1[1]]
        return res[m-1][n-1]
        