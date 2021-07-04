class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        s = ''
        ptr = self.head

        while ptr:
            s += str(ptr.val) + ' -> '
            ptr = ptr.next
        
        s = s.strip(' -> ')

        if len(s)==0:
            return None
        else:
            return s

    def listLength(self):
        n = 0
        ptr = self.head
        while ptr:
            n += 1
            ptr = ptr.next
        return n
    
    def addNode(self, node, pos):
        n = 1
        ptr = self.head
        if pos == 0:
            node.next = self.head
            self.head = node
        else:
            while n <= pos:
                if ptr.next:
                    prev = ptr
                    ptr = ptr.next
                    n += 1
                else:
                    print("Position number exceeding LinkedList length.")
                    return None
            node.next = ptr
            prev.next = node
            #ptr.next = node
    
    def deleteNode(self, pos):
        ptr = self.head
        n = 1
        if pos == 0:
            self.head = ptr.next
            ptr.next = None
        else:
            while n <= pos:
                if ptr.next:
                    prev = ptr
                    ptr = ptr.next
                    n += 1
                else:
                    print("Position number exceeding LinkedList length.")
                    return None
            print(ptr.val)
            prev.next = ptr.next
            ptr = None


                

l0 = Node(0)
l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l = LinkedList(l0)
l.head = l0
l0.next = l1
l1.next = l2
l2.next = l3
l4 = Node(4)
#l.addNode(l4, 5)
l.deleteNode(4)
print(l)
print(l.listLength())