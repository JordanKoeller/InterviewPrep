
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(headNode):
    if headNode and headNode.next == None:
        return headNode
    nextNode = headNode.next
    currNode = headNode
    currNode.next = None
    while nextNode:
        nextNextNode = nextNode.next
        nextNode.next = currNode
        currNode = nextNode
        nextNode = nextNextNode
    return currNode


def testReverse():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    printList(a)
    rev = reverse(a)
    print("Reversed below")
    printList(rev)

def printList(head):
    rover = head
    ret = []
    while rover:
        ret.append(rover.value)
        rover = rover.next
    print(ret)

testReverse()
