import unittest

def is_properly_nested(S):
    """
    Given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
    For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

    A string S consisting of N characters is called properly nested if:
        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.
        For example, string "(()(())())" is properly nested but string "())" isn't.

    Args:
        S: a string consisting only of the characters "(" and/or ")"

    This solution obtained perfect score with O(N)
    """
    
    if len(S) == 0:
        return 1
    
    if S[0] == ')':
        return 0
    
    left_brackets = S.replace(')','')
    right_brackets = S.replace('(', '')
    
    if len(left_brackets) != len(right_brackets):
        return 0
    
    remaining_left_brackets = 0
    
    for s in S:
        if s == '(':
            remaining_left_brackets += 1
        else:
            remaining_left_brackets -= 1
        
        if remaining_left_brackets < 0:
            return 0
        
    if remaining_left_brackets == 0:
        return 1
    else:
        return 0
    

class Test(unittest.TestCase):
    
    def test_unequal_number_of_left_and_right_brackets(self):
        self.assertEqual(is_properly_nested("()("), 0)
    
    def test_wrong_order(self):
        self.assertEqual(is_properly_nested("())("), 0)
        
    def test_start_with_right_bracket(self):
        self.assertEqual(is_properly_nested(")()()"), 0)
        
    def test_nested(self):
        self.assertEqual(is_properly_nested("(()())(())()"), 1)
        
    def test_empty_string(self):
        self.assertEqual(is_properly_nested(''), 1)
    
if __name__ == '__main__':
    unittest.main()