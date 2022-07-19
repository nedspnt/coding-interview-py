def minimum_possible_abs_of_sum(A):
    """ Given an unsorted array A of size N, and the value p, where 0 < p < N,
    Find the minimum possible value of abs(sum(A[p:]) - sum(A[:p])_
    
    """
    
    min_diff = None
    
    total_sum = sum(A)
    left_sum = 0

    for i in range(len(A)-1):
        
        left_sum = left_sum + A[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        
        if min_diff is None or diff < min_diff:
            min_diff = diff

    return min_diff