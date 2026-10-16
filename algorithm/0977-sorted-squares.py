# LeetCode 977 有序数组的平方  https://leetcode.cn/problems/squares-of-a-sorted-array/
# 思路：双指针——最大值一定在两端，从两端向中间夹，大的平方从结果末尾往前填
# 复杂度：时间 O(n)，空间 O(n)


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        for pos in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] * nums[left]
                left += 1
            else:
                res[pos] = nums[right] * nums[right]
                right -= 1
        return res
