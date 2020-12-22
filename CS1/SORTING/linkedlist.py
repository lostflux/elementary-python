class Node:
    def __init__(self, data):
        self.data = data  # instance variable to store the data
        self.next = None  # instance variable with address of next node

    def find(self, x):
        if self.data == x:
            return self
        else:
            if self.next:
                return self.next.find(x)
            else:
                temp = Node("Not Found!")
                return temp


#
# # write your code here:
# head = Node(0)
# current = Node(0)
# head.next = current
# sum = 0
# while current.data < 100:
#     sum += current.data
#     # print(sum)
#     current.next = Node(current.data + 2)
#     current = current.next

# Print the data of the list in order:
# current = head  # copy the address of the head node into node
# while current != None:
#     print(current.data)
#     current = current.next


head = Node("Maine")
another_node = Node("Idaho")
head.next = another_node
a_third_node = Node("Utah")
another_node.next = a_third_node

print("Found:  " + str(head.find("Utah").data))