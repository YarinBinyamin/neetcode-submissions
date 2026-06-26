"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_dic = {}
        dum = head
        sen_head = Node(-1,None, None)
        prev = sen_head
        while dum:
            node = Node(dum.val,None, None)
            hash_dic[dum] = node
            prev.next=node
            prev = prev.next
            dum = dum.next
        dum1 = head
        dum2 = sen_head.next
        while dum1:
            dum2.random = hash_dic[dum1.random] if dum1.random else None
            dum1 = dum1.next
            dum2 =dum2.next
        return sen_head.next