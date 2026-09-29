# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Split the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rlist = slow.next
        slow.next = None

        # Reverse the second linkedlist
        prev = None
        while rlist:
            temp = rlist.next
            rlist.next = prev
            prev = rlist
            rlist = temp
        
        print(rlist)
    
        # Merge the two lists
        curr = head
        print(curr)
        while prev:
            tmp1, tmp2 = curr.next, prev.next
            curr.next = prev
            prev.next = tmp1
            curr = tmp1
            prev = tmp2
        




