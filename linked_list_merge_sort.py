from linked_list import Linked_list

def merge_sort(linked_list):
    '''
    Sorts a linked list in alphabetical order
    - Recursively divides the linked list into sublists containing single nodes
    - Repeatedly  merges the sublists to produce a single linked list 
    '''

    if linked_list.size() == 1 or linked_list.head == None:
        return linked_list
    
    left_hallf, right_half = split(linked_list)
    left = merge_sort(left_hallf)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):

    current = list.head
    left = Linked_list()
    right = Linked_list()

    if list.head == None or list == None:
        left = list
        right = None
        return left, right
    

    mid = list.size() // 2
    i = 0

    

    
    while current:
        if i <= mid:
            left.add(current)
            i += 1
        else:
            right.add(current)
        
        current = current.next_node

    return left, right
        
def merge(left, right):
    sorted = Linked_list()

    left_current = left.head
    right_current = right.head
    
    while left_current and right_current:
        if left_current > right_current:
            sorted.add(left_current)
            left.next_node
        else:
            sorted.add(right_current)
            right.next_node
    
    return sorted


l = Linked_list()
l.add(7)
l.add(3)
l.add(6)
l.add(2)
l.add(5)
l.add(1)
l.add(9)
l.add(4)
l.add(8)

print(l)

sorted_list = merge_sort(l)
print(sorted_list)


    
