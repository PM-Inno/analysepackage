def sum_array(array):
    '''Return sum of all items in array
     Args:
        items (array): list or array-like object containing numerical values.

     Returns:
        int or float : sum of all items

     Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24
    '''
    count =0
    for i in array:
        count += i
    return count


def fibonacci(n):
    '''Return nth term in fibonacci sequence
    Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >>> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    '''
    if n<=1:
        return n
    else:
        return fibonacci(n-1) +fibonacci(n-2)


def factorial(n):

    '''Return n!
    Args:
         n (int): term to calculates 
    
    Returns:
        int: number we get after multiplying every umbeer from 1 to n

    Examples:
    >>> factorial(3)
     2
     >>> factorial(4)
     24
    >>> factorial(5)

    '''
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

  
def reverse(word):
       s = ""
       for ch in word:
           s = ch + s
       return s
        #if len(word) == 0:
            #return word
        #else:
            #return reverse(word[1:]) + word[0]
