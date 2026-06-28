# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        q = head
        r = None

        if head == None or head.next == None:
            return head

        while q:
            r = q.next
            q.next = p

            p = q
            q = r

        return p


