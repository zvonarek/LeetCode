# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # once fast reaches end
        fast = slow = head
        # slow will be at the middle since it travels half as fast  
        while fast and fast.next:
            # this will ensure that at the very least fast.next will be non-null
            try: 
                fast = fast.next.next
            except: 
                fast = fast.next
                
            slow = slow.next
        
        return slow