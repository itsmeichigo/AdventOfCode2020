# Given the head of a LinkedList and a number ‘k’, 
# reverse every alternating ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, 
# reverse it too.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_alternate_k_elements(head, k):
    if head is None or k <= 1: return head
    p, q = 1, 1
    current = head
    should_reverse = True
    while current is not None:
        q += 1
        current = current.next
        if q - p + 1 == k:
            if should_reverse:
                current = current.next
                head = reverse_sublist(head, p, q)
            p = q + 1
            should_reverse = not should_reverse
    if q > p and should_reverse:
        head = reverse_sublist(head, p, q)
    return head

def reverse_sublist(head, p, q):
    previous, current = None, head
    i = 1
    while current is not None and i < p:
        previous = current
        current = current.next
        i += 1
    last_node, start = previous, current
    while current is not None and i < q+1:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        i += 1
    if last_node is not None: last_node.next = previous
    else: head = previous
    start.next = current

    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
