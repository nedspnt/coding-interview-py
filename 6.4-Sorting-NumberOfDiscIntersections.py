import unittest

MAX_INTERSECTIONS = 10000000

def NumberOfDiscIntersectionsSlow(A):
    """
    This solution is correct, but bad performance O(N^2)
    """
    
    num_intersections = 0
    
    tracking = dict()
    
    for i in range(len(A)):
        tracking[i] = dict()
        for j in range(len(A)):
            tracking[i][j] = True
            
            try:
                redundant = tracking[j][i]
            except:
                redundant = False
            
            if i != j and not redundant:
            
                min_i, max_i = -A[i]+i, A[i]+i
                min_j, max_j = -A[j]+j, A[j]+j
                
                # circle i on the left
                if i < j and max_i >= min_j:
                    num_intersections += 1
                    
                # circle j on the left
                elif j < i and max_j >= min_i:
                    num_intersections += 1
                    
                if num_intersections > MAX_INTERSECTIONS:
                    return -1
    
    return num_intersections

def NumberOfDiscIntersectionsFast(A):
    """
    This solution achieve a perfect score O(N * log(N))
    
    https://github.com/johnmee/codility/blob/master/ex-6-4-NumberOfDiscIntersections.py
    """

    num_intersections = 0
    
    left_edges = []
    right_edges = []
    len_A = len(A)
    
    # store all min max
    for i in range(len_A):
        left_edges.append(-A[i]+i)
        right_edges.append(A[i]+i) 
    left_edges.sort() 
    right_edges.sort() 
    
    
    len_left_edges = len_right_ages = len_A
    left_i = 0
    
    for right_i in range(len_right_ages):
        
        right_edge = right_edges[right_i] 

        while left_i < len_left_edges and left_edges[left_i] <= right_edge:
            
            left_i += 1
            num_intersections += left_i - right_i - 1
                
            if num_intersections > MAX_INTERSECTIONS:
                return -1
    
    return num_intersections

NumberOfDiscIntersections = NumberOfDiscIntersectionsFast

class Test(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(NumberOfDiscIntersections([1,5,2,1,4,0]), 11)
    
if __name__ == '__main__':
    unittest.main()
