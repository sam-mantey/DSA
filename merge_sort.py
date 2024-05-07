def merge_sort(list):
    '''
    Sorts a list using the divide and conquer approach 
    This function accepts a list as an argument and splits it in to two recursively until it has two elements left 
    then it sorts the two elements then merge them
    '''
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)




def split(list):
    '''
    Splits list into two
    '''

    mid = len(list)//2

    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    '''
    combines the left and right lists while sorting it 
    '''

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else: 
            sorted_list.append(right[j])
            j += 1
        
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    
    return sorted_list


list = [9, 4, 6, 3, 7, 2, 1, 5, 8, 0]
soted = merge_sort(list)


def verify(sorted):
    if len(sorted) <= 1:
        return True
    
    return sorted[0] < sorted[1] and verify(sorted[1:])

print(verify(soted))