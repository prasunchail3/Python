"""
This program calculates the nth Fibonacci number in O(log(n)).
It's possible to calculate F(1000000) in less than a second.
"""
#------------------------------------Actual Computation---------------------#
def fastExpo(n):
    if n == 1:
      return [[1, 1], [1, 0]]  
    matrix = fastExpo(n//2)
    matrix1 = [[0, 0], [0, 0]]
    matrix1[0][0] = matrix[0][0] ** 2 + (matrix[0][1] * matrix[1][0])
    matrix1[1][1] = matrix[1][1] ** 2 + (matrix[0][1] * matrix[1][0])
    matrix1[0][1] = matrix[0][1] * (matrix[0][0] + matrix[1][1])
    matrix1[1][0] = matrix[1][0] * (matrix[0][0] + matrix[1][1])
    if n % 2 == 0:
        return matrix1[:]
    else:
        matrix2 = [[0, 0], [0, 0]]
        matrix2[0][0] = matrix1[0][0] + matrix1[1][0]
        matrix2[1][1] = matrix1[0][1]
        matrix2[0][1] = matrix1[0][1] + matrix1[1][1]
        matrix2[1][0] = matrix1[0][0]
        return matrix2[:]

"""
Assuming the 0th element to be 0, 1st element to be 1, 2nd to be 1 and so on
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fastExpo(n)[1][0]

#---------------------------------------------------------------------------#
#--------------------------------Input Statements---------------------------#
print('Enter the value of n : ')
n = int(input())
n -= 1
if n < 0:
    print('Invvalid input')
else:
    print('The fibonacci number at position ', n+1, ' is : ', fibonacci(n))
#---------------------------------------------------------------------------#
