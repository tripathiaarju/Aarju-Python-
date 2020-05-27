import numpy as np

def gen_vander_matrix(ipvector, n, increasing=False):
    if not increasing:
        op_matx = np.array( [x ** (n - 1 - i) for x in ipvector for i in range( n )] ).reshape( ipvector.size, n )
    elif increasing:
        op_matx = np.array( [x ** i for x in ipvector for i in range( n )] ).reshape( ipvector.size, n )
    return op_matx

inputvector = np.array( [1, 2, 3, 4, 5] )
no_col_opmat = 3
op_matx_dec_order = gen_vander_matrix( inputvector, no_col_opmat, False )
op_matx_inc_order = gen_vander_matrix( inputvector, no_col_opmat, True )
print( "The input array is:", inputvector, "\n" )
print( "Number of columns in output matrix should be:", no_col_opmat, "\n" )
print( "Vander matrix of the input array in decreasing order of powers:\n\n", op_matx_dec_order, "\n" )
print( "Vander matrix of the input array in increasing order of powers:\n\n", op_matx_inc_order, "\n" )
inputvector = np.array( [1, 2, 4, 6, 8, 10] )
no_col_opmat = 5
op_matx_dec_order = gen_vander_matrix( inputvector, no_col_opmat, False )
op_matx_inc_order = gen_vander_matrix( inputvector, no_col_opmat, True )
print( "The input array is:", inputvector, "\n" )
print( "Number of columns in output matrix should be:", no_col_opmat, "\n" )
print( "Vander matrix of the input array in decreasing order of powers:\n\n", op_matx_dec_order, "\n" )
print( "Vander matrix of the input array in increasing order of powers:\n\n", op_matx_inc_order, "\n" )

'''OUTPUT
The input array is: [1 2 3 4 5] 

Number of columns in output matrix should be: 3 

Vander matrix of the input array in decreasing order of powers:

 [[ 1  1  1]
 [ 4  2  1]
 [ 9  3  1]
 [16  4  1]
 [25  5  1]] 

Vander matrix of the input array in increasing order of powers:

 [[ 1  1  1]
 [ 1  2  4]
 [ 1  3  9]
 [ 1  4 16]
 [ 1  5 25]] 

The input array is: [ 1  2  4  6  8 10] 

Number of columns in output matrix should be: 5 

Vander matrix of the input array in decreasing order of powers:

 [[    1     1     1     1     1]
 [   16     8     4     2     1]
 [  256    64    16     4     1]
 [ 1296   216    36     6     1]
 [ 4096   512    64     8     1]
 [10000  1000   100    10     1]] 

Vander matrix of the input array in increasing order of powers:

 [[    1     1     1     1     1]
 [    1     2     4     8    16]
 [    1     4    16    64   256]
 [    1     6    36   216  1296]
 [    1     8    64   512  4096]
 [    1    10   100  1000 10000]]
'''