#Write a program to find the node at which the intersection of two singly linked lsits begins.

#Definition for singly linked list.
# class ListNode(object):
#       def __init__(self, x):
#           self.val = x
#           self.next = None

# Variable Table
# heada = node1
# headb = node2
# pointera = heada
# pointerb = headb

class Solution(object):
    def getintersectionnode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None and headB == None:
            print("Heads are empty")
            return None

        pointera = heada
        pointerb = headb

        while pointera != pointerb:
            if pointera == None:
                pointera = headb
            else
                pointera = pointera.next
