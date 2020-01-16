# A little look at linked lists: below is inserting a tail of a linked list from HackerRank
# reference: https://stackoverflow.com/questions/35559632/insert-a-node-at-the-tail-of-a-linked-list-python-hackerrank

# The code immediately below is a verbatim copy, so this disclaimer is being placed here in attempt to avoid
# copyright issues; the reference mentioned above is where the information came from.

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def Insert(head, data):
        if (head == None):
            head = Node(data)
        else:
            current = head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
            return head
