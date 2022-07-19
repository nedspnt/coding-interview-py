import unittest

def num_of_diversible_int(A, B, K):
    """
    Given the range of integers i, A <= i <= B, find the number of integers divisible by K
    
    This solution obtained perfect score with O(1)
    
    Args:
        A: starting integer within range of 0 to any large integers
        B: ending integer within range of 0 to any large integers
    
    """
    
    if A == B:
        if K == A:
            return 1
        if A == 0:
            return 1
        if A % K == 0:
            return 1
    
    if A % K == 0:
        min_divisible_int = (A // K) * K
    else:
        min_divisible_int = ((A // K) + 1) * K
        
    max_divisible_int = B - (B % K)
    
    return int((max_divisible_int - min_divisible_int) / K) + 1

class Test(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(num_of_diversible_int(1,10,3), 3)
        
    def test_divisible_left_edge(self):
        self.assertEqual(num_of_diversible_int(6,11,2), 3)
    
    def test_divisible_right_edge(self):
        self.assertEqual(num_of_diversible_int(7,12,2), 3)
        
    def test_divisible_both_edges(self):
        self.assertEqual(num_of_diversible_int(6,12,2), 4)
        
    def test_A_equals_B_equals_K(self):
        self.assertEqual(num_of_diversible_int(5,5,5), 1)
        
    def test_A_equals_B_with_indivisible_K(self):
        self.assertEqual(num_of_diversible_int(5,5,3), 0)
        
    def test_A_equals_B_with_divisible_K(self):
            self.assertEqual(num_of_diversible_int(10,10,5), 1)
        
    def test_A_equals_B_different_K(self):
        self.assertEqual(num_of_diversible_int(5,5,3), 0)
        
    def test_zeroes_A_B_with_positive_K(self):
        self.assertEqual(num_of_diversible_int(0,0,11), 1)
        
        
if __name__ == '__main__':
    unittest.main()