import numpy as np

#1
hours=np.arange(0,21+1,3)
line=np.linspace(0,1,5)
zeros=np.zeros(6,dtype=int)
unknown_table=np.full((2,3),-1)
identity=np.full((3,3),1)
print(hours,hours.shape,hours.ndim,hours.size,hours.dtype)

#2
print(hours[2],hours[-1],hours[2:6],hours[::2],hours[::-1])

#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape,temperatures.ndim,temperatures.size,temperatures[1,2],temperatures[0,:],temperatures[:,-1],temperatures[:2,1:],temperatures[:2,1:-1])

#4
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:3,:].shape,matrix[-2:,:].shape,matrix[:,:2].shape,matrix[1:4,2:5].shape,matrix[-2:,-2:].shape)

#5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
changed_hours = hours.copy()
#copy нужен, чтобы исходный массив не менялся
print(hours)
changed_hours[2:5]=99
changed_hours[::2]=-1
print(changed_hours)
changed_matrix = matrix.copy()
#copy нужен, чтобы исходная матрица не менялся
changed_matrix[1:2,:]=0
changed_matrix[:,-1]=-1
changed_matrix[1:4,1:4]=100
print(matrix)
print(changed_matrix)

#6
numbers=np.arange(0,12)
table=numbers.reshape(3,4)
transposed=table.T
print(numbers.shape,table.shape,transposed.shape)
#reshape(5,3) вызовет ошибку, так как 12 на 5 не делится нацело, а в reshape(3,4) 3 и 4 оба делители числа 12
