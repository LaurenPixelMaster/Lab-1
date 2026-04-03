import unittest
import Matrix

class test_matrix(unittest.TestCase):
    def test1(self):
        a=[[1,2],
           [3,4]
        ]
        b=[
           [5,6],
           [7,8]
        ]
        answer=[[19,22],[43,50]]
        self.assertEqual(Matrix.matrix_multiply(a,b), answer)
    def test2(self):
        a=[[1,2,3],
           [4,5,6]
        ]
        b=[
           [7,8],
           [9,10],
           [11,12]
        ]
        answer=[[58,64],[139,154]]
        self.assertEqual(Matrix.matrix_multiply(a,b), answer)
    def test3(self):
        a=[]
        b=[
           [5,6],
           [7,8]
        ]
        with self.assertRaises(ValueError):
            Matrix.matrix_multiply(a,b)
    def test_empty_matrix(self):
        A = []
        B = [[1]]
        with self.assertRaises(ValueError):
            Matrix.matrix_multiply(A, B)
    def test_non_rectangular_matrix(self):
        A = [[1, 2], [3]]  
        B = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            Matrix.matrix_multiply(A, B)
    def test_zero_matrix(self):
        A = [[0, 0], [0, 0]]
        B = [[1, 2], [3, 4]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(Matrix.matrix_multiply(A, B), expected)
    def test_single_element_matrix(self):
        A = [[5]]
        B = [[7]]
        expected = [[35]]
        self.assertEqual(Matrix.matrix_multiply(A, B), expected)
    def test_negative_numbers(self):
        A = [[-1, -2], [-3, -4]]
        B = [[5, 6], [7, 8]]
        expected = [[-19, -22], [-43, -50]]
        self.assertEqual(Matrix.matrix_multiply(A, B), expected)
    def test_float_numbers(self):
        A = [[1.5,2.0], [3.0,4.5]]
        B = [[5.0, 6.5], [7.5, 8.0]]
        expected = [[22.5, 25.75], [48.75, 55.5]]
        self.assertEqual(Matrix.matrix_multiply(A, B), expected)
    def test_mismatchmatrix_matrix(self):
        A = [[5,6,7], ]  
        B = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            Matrix.matrix_multiply(A, B)
unittest.main()