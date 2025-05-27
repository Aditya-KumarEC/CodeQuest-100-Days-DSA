class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def linked_list(num):
    if not num:
        return None
    head = Node(num[0])
    current = head
    for n in num[1:]:
        current.next = Node(n)
        current = current.next
    return head

def print_list(head):
    print("Linked List: ",end=" ")
    current = head
    while current :
        print(current.data,end=" ->"if current.next else"")
        current = current.next
    print()
number = list(map(int,input("Enter numbers: ").split()))
head = linked_list(number)
print_list(head)