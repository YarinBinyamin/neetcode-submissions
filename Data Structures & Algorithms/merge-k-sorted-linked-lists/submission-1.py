# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  

    def mergeTwoLists(self,  list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            head1= list1
            head2= list2
            dummy = ListNode(-1)
            head_of_dummy = dummy
            while head1 and head2:
                #print(f" {head1.val} {head2.val}")
                if head1.val <= head2.val:
                        dummy.next = head1
                        head1 = head1.next
                else:
                    dummy.next = head2
                    head2 = head2.next
                dummy = dummy.next
            if head1 is None: 
                dummy.next = head2
            elif head2 is None:
                dummy.next = head1 
            return head_of_dummy.next    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) != 1:
            index = 0
            while index < len(lists) -1:
                lists[index] = self.mergeTwoLists(lists[index],lists[index+1])
                index+=2
            index=1
            while index < len(lists):
                del lists[index]   
                index+=1
        #self.print_ll(lists[0] )
        return lists[0]     
        