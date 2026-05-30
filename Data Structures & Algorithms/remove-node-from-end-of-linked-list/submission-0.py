# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        save_head = ListNode(-1)
        save_head.next = head
        dummy = head
        length = 0
        while dummy :
            length+=1
            dummy=dummy.next
        removal_index = length - n 
        prev = save_head
        cur = head
        while removal_index > 0  and cur:
            prev = cur
            cur = cur.next
            removal_index -=1
        prev.next = cur.next
        return save_head.next