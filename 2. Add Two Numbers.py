# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        now = l1
        n1 = str(l1.val)
        while now.next != None:
            now = now.next
            n1 += str(now.val)
        
        now = l2
        n2 = str(l2.val)
        while now.next != None:
            now = now.next
            n2 += str(now.val)

        n1 = n1[::-1]
        n2 = n2[::-1]
        n = str(int(n1) + int(n2))

        ans = None
        for i in range(len(n)):
            value = int(n[i])
            ans = ListNode(value, ans)
        return ans