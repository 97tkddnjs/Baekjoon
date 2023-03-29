from typing import List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, value):
#         new_node = ListNode(value)

#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = self.tail.next



# <- 배열로 생각함~
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rtype= True

        length = len(head)

        size = length//2

        left = head[:size]
        right= head[size if length % 2 ==0 else size+1 :]

        for i in range(size):
            if left[i] != right[length-1 -i]:
                return False
        
        return rtype


