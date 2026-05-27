# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carr = 0

        while l1 and l2:
            if l1 is None:
                l1.vall=0
            if l2 is None:
                l2.val=0

            total = l1.val+l2.val+carr
            curr.next = ListNode(total%10)
            carr = (l1.val+l2.val)//10

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        if carr:
            curr.next = ListNode(carr)
        return dummy.next