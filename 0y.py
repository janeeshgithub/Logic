class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        middle = self.getMiddle(head)
        right_half = middle.next
        middle.next = None
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(right_half)
        return self.merge(left_sorted, right_sorted)

    def getMiddle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

    solution = Solution()
    print("Original List:")
    printList(head)

    sorted_head = solution.mergeSort(head)
    print("\nSorted List:")
    printList(sorted_head)
