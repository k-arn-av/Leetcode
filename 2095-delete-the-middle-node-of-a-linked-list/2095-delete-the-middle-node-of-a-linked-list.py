# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middlenode=slow
        slow=head
        if slow and slow.next:
            while slow.next!=middlenode:
                slow=slow.next
            
            slow.next=middlenode.next
            return head
        return None
            

        


        