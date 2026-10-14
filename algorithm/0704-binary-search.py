# LeetCode 704 二分查找  https://leetcode.cn/problems/binary-search/
# 思路：闭区间 [left, right]，每次和 nums[mid] 比较后砍掉不可能的一半
# 复杂度：时间 O(log n)，空间 O(1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
