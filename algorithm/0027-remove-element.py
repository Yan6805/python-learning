# LeetCode 27 移除元素  https://leetcode.cn/problems/remove-element/
# 思路：快慢指针——k 是"下一个写入位置"，把不等于 val 的元素依次写到前面，val 被自然覆盖
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k
