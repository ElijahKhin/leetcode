from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        while headA:
            d[headA] = 1
            headA = headA.next
        while headB:
            if d.get(headB, 0) == 1:
                return headB
            headB = headB.next
        return None


if __name__ == "__main__":
    lstA = [4,1]
    lstB = [5,6,1]
    intersect = [8,4,5]
    headA = ListNode(lstA[0])
    headB = ListNode(lstB[0])
    runA = headA
    runB = headB
    for i in range(1, len(lstA)):
        runA.next = ListNode(lstA[i])
        runA = runA.next

    for i in range(1, len(lstB)):
        runB.next = ListNode(lstB[i])
        runB = runB.next

    for i in range(len(intersect)):
        new_one = ListNode(intersect[i])
        runA.next = runB.next = new_one
        runA = runA.next
        runB = runB.next

    sol = Solution()
    print((sol.getIntersectionNode(headA, headB)).val)
