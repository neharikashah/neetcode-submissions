# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n == 0:
            return head
        
        slow = head
        fast = head
        while n:
            fast = fast.next
            n-=1

        if not fast:
            return head.next

        pre = None
        while fast:
            pre = slow
            fast = fast.next
            slow = slow.next


        pre.next = slow.next
        return head
        