def greeting ():
	print ("hello")

def matrix_multiply_usingnumpy(a,b):
#	return [[19,22],[43,50]]
	import numpy
	a=numpy.array(a)
	b=numpy.array(b)
	return a.dot(b).tolist()

def matrix_multiply(A, B):
    if len(A) == 0 or len(B) == 0:
        raise ValueError("Matrics cannot be empty")
    row_length_A = len(A[0])
    for row in A:
        if len(row) != row_length_A:
            raise ValueError("Matrix A is not rectangular")
    row_length_B = len(B[0])
    for row in B:
        if len(row) != row_length_B:
            raise ValueError("Matrix B is not rectangular")
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Matrices have incompatible dimensions for multiplication.")
    result = []
    for i in range(rows_A):
        result.append([0] * cols_B)
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
#greeting ()