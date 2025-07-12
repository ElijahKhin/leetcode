from typing import Optional

def initList(head, nums):
    n = len(nums)
    for i in range(1, n):
        node = ListNode(nums[i])
        head.next = node
        head = node

class ListNode:
    def __init__(self, val_=0, next_=None):
        self.val = val_
        self.next = next_

    def print(self):
        print(self.val)
        while self.next != None:
            self.val = self.next.val
            self.next = self.next.next
            print(self.val)



class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        now = head
        while now:
            prev = now
            now = now.next
            while now and now.val == val:
                now = now.next
                prev.next = now
        return head

if __name__ == "__main__":
    nums = [1,2,6,3,4,5,6]
    head = ListNode(1)
    initList(head, nums)
    head.print()
