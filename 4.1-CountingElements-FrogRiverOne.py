import unittest

def frog_jump(X, A):
    """ Find the earliest time the frog can jump

    Args:
        X: the number of steps the frog needs to jump in order to get to the other side
        A: an array where A[K] indicates the position where one leaf falls at time K, e.g A[1] = 2 means at second 1 there is a leaf appears at position 2
    """
    
    required_steps = set(range(1, X+1))
    
    if required_steps.difference(set(A)) != set():
        return -1
    
    for i in range(len(A)):
        required_steps.discard(A[i])
        if required_steps == set():
            return i

class Test(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(frog_jump(3, [1,1,2,1,3,3]), 4)
    
    def test_can_never_jump(self):
        self.assertEqual(frog_jump(10, [2,3,1,2]), -1)
        
    def test_leafs_fall_to_non_jumpabe_positions(self):
        self.assertEqual(frog_jump(4, [5,6,8,9]), -1)

if __name__ == '__main__':
    unittest.main()