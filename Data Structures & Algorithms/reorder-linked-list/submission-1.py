# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Split linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        # Reverse list2
        list2head = None
        while list2:
            temp = list2.next
            list2.next = list2head
            list2head = list2
            list2 = temp

        curr, curr2 = list2head, head
        while curr:
            tmp1, tmp2 = curr2.next, curr.next
            curr2.next = curr
            curr.next = tmp1
            curr = tmp2
            curr2 = tmp1
        

