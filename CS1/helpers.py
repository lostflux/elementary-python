def print_ll(head):
    n = head
    while n.next is not None:
        print(n.data, end = "-->" )
        n = n.next

    print(n.data)


def build_ll(glist):
    if len(glist) == 0:
        return None

    n = Node(glist[0])
    head = n
    for i in range(1, len(glist)):
        new_node = Node(glist[i])
        # n.set_next(new_node)
        n.next = new_node
        n = new_node
    return head