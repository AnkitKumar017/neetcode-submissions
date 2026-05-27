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

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1+val2+carr
            curr.next = ListNode(total%10)
            carr = (val1+val2)//10

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        if carr:
            curr.next = ListNode(carr)
        return dummy.next