def recursive_binary(list, target):

    if len(list) == 0:
        return False
    
    midpoint = len(list) // 2

    if list[midpoint] == target:
        return True
    elif list[midpoint] < target:
        return recursive_binary(list[midpoint + 1:], target)
    else:
        return recursive_binary(list[: midpoint], target)
    

print(recursive_binary([1,2,3,4,5], 9))