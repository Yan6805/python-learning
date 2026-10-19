# LeetCode 59 螺旋矩阵 II  https://leetcode.cn/problems/spiral-matrix-ii/
# 思路：一圈一圈剥壳。四条边按 上→右→下→左 的顺序填，每条边都取闭区间
#      （range 终点 +1；反向的下边/左边 stop 写另一端点的前一位）；
#      每填完一条边就立刻把这条边界往里缩 1，角落既不会重复也不会漏。
#      n 为奇数时中心格由最后一圈的"上边"自动填上。
# 复杂度：时间 O(n^2)，空间 O(1)（不计返回的矩阵）


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        count = 1
        m = [[0] * n for _ in range(n)]
        top = left = 0
        right = bottom = n - 1
        while count <= n * n:
            for j in range(left, right + 1):
                m[top][j] = count
                count += 1
            top += 1
            for i in range(top, bottom + 1):
                m[i][right] = count
                count += 1
            right -= 1
            for j in range(right, left - 1, -1):
                m[bottom][j] = count
                count += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                m[i][left] = count
                count += 1
            left += 1
        return m
