# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None
    
        curr = None
        listptr1, listptr2 = None, None
        if list1.val <= list2.val:
            curr = list1
            listptr1, listptr2 = curr.next, list2
        else:
            curr = list2
            listptr1, listptr2 = list1, curr.next
        
        temp = curr
        
        while listptr1 is not None and listptr2 is not None:
            if listptr1.val <= listptr2.val:
                curr.next = listptr1
                listptr1 = listptr1.next
                curr = curr.next
            else:
                curr.next = listptr2
                listptr2 = listptr2.next
                curr = curr.next
        
        while listptr1 is not None:
            curr.next = listptr1
            listptr1 = listptr1.next
            curr = curr.next
        while listptr2 is not None:
            curr.next = listptr2
            listptr2 = listptr2.next
            curr = curr.next
        
        return temp

        

        
