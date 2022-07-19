import unittest

def right_rotation(A, K):
    """ Rotate an array A to the right K times
    """
    
    len_A = len(A)
    
    if len_A == 0:
        return []
    
    A = A * 2
    K = K % len_A
    i = len_A - K

    return A[i:i+len_A]

class Test(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(right_rotation([3,8,9,7,6], 3), [9, 7, 6, 3, 8])
        
    def test_empty(self):
        self.assertEqual(right_rotation([], 4), [])
        
    def test_zeroes(self):
        self.assertEqual(right_rotation([0,0,0], 1), [0,0,0])
        
    def test_one_element(self):
        self.assertEqual(right_rotation([2], 2), [2])
        
    def test_two_elements(self):
        self.assertEqual(right_rotation([2,1], 2), [2,1])
        
    def test_k_elements(self):
        self.assertEqual(right_rotation([3,2,1], 3), [3,2,1])
        
    def test_k_more_than_array_len(self):
        self.assertEqual(right_rotation([3,4,5], 10), [5,3,4])

if __name__ == '__main__':
    unittest.main()
