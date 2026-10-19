# LeetCode 209 长度最小的子数组  https://leetcode.cn/problems/minimum-size-subarray-sum/
# 思路：滑动窗口。right 只负责向右扩；当窗口和 >= target 时，再从左边收缩并记录最小长度。
#      因为元素全为正数，收缩时窗口和单调减小，降到 target 以下即可停 —— left 单调不减、right 不回退，整体 O(n)。
# 复杂度：时间 O(n)，空间 O(1)
# 备注：left == 0 等价于"内层收缩从未执行过"等价于"无解"，因此用它当哨兵返回 0。


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        right = 0
        min_count = len(nums)
        while right < len(nums):
            total += nums[right]
            right += 1
            while total >= target:
                count = right - left
                if min_count >= count:
                    min_count = count
                total = total - nums[left]
                left += 1
        return 0 if (right == len(nums) and total < target and left == 0) else min_count
