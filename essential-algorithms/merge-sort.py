import unittest

def merge_sort(arr):

    if len(arr) == 1:
        return arr

    mid_idx = len(arr) // 2

    L = arr[:mid_idx]
    R = arr[mid_idx:]

    merge_sort(L)
    merge_sort(R)

    def merge(L, R):
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr

    return merge(L, R)


class Test(unittest.TestCase):

    def test_example(self):
        self.assertEqual(merge_sort([5,4,2,1,3]), [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()