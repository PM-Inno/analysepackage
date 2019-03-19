def bubble_sort(items):

    '''Return array of items, sorted in ascending order
    Args:
        items: a list of items
    Returns:
          array/list that is sorted in order
          
    Examples 
    >>>bubble_sort([7,11,2,8,9,])
     [2,7,8,9,11]
     >>>bubble_sort([
         
    '''
    for i in range(0,len(items)-1):
        for j in range(0,len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items 


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list 
    return merge(i1, i2)
# Merge function.
def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list


def quick_sort(items):
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
