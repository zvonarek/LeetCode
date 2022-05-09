# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start with adding a node to the left of the head node; prev.val = Null
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            # as you go down the List with curr.next, redirct to the prev nodd
            prev = curr
            curr = temp
        # return prev since it will be at the reverse head 
        return prev
        
        
       
        
 
        
            
        
    
        