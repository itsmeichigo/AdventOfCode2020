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

def reverse_sub_list(head, p, q):
    if p == q: return head
    previous, current = None, head
    index = 1
    while current is not None and index < p: 
        previous = current
        current = current.next
        index += 1
    last_node, start = previous, current
    while current is not None and index < q + 1:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        index += 1

    if last_node is not None:
        last_node.next = previous
    else:
        head = previous

    start.next = current
    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()