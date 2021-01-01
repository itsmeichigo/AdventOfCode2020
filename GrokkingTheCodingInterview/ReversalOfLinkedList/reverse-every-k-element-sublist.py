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


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None: return head
    current = head
    p, q = 1, 1
    while current is not None:
        q += 1
        current = current.next
        if q - p + 1 == k:
            head = reverse_sublist(head, p, q)
            p = q + 1
    if q > p:
        head = reverse_sublist(head, p, q)
    return head

def reverse_sublist(head, p, q):
    previous, current, i = None, head, 1
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
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()