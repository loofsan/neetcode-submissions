# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count, curr = 0, head
        while curr:
            count+=1
            curr = curr.next
        
        removeIndex = count - n

        if removeIndex == 0:
            return head.next
        
        curr2 = head
        for i in range(count-1):
            if (i+1) == removeIndex:
                curr2.next = curr2.next.next
                break
            curr2 = curr2.next
        
        return head