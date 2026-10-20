# LeetCode 203 移除链表元素  https://leetcode.cn/problems/remove-linked-list-elements/
# 思路：虚拟头结点 dummy.next = head —— 让"删头结点"和"删中间结点"共用同一套逻辑，省掉对 head 的特判。
#      pre 始终是 cur 的前一个结点：命中 val 就让 pre.next 跳过 cur，否则 pre 跟着前进；cur 每轮必前进。
#      最后返回 dummy.next 而不是 head（原来的 head 可能正好是要删的那个）。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur != None:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
