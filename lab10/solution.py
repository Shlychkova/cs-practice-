import numpy as np

def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows*columns).reshape(rows,columns).tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    arr=np.array(matrix)
    return arr[row_start:row_stop,column_start:column_stop].tolist()
def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    arr=np.asarray(matrix).copy()
    arr[row_start:row_stop,column_start:column_stop]=value
    return arr.tolist()
def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    mat=np.array(matrix)
    v=np.array(vector)
    return (mat @ v).tolist()
def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return (np.array(left)@ np.array(right)).tolist()
def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.array(matrix).T.tolist()
def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    res=np.lilang.solve(np.array(matrix),np.array(vector))
    return np.round(res,6).tolist()
def tensor_channel_mean(tensor: list) -> list:
    arr=np.array(tensor)
    return np.mean(arr,axis=-1).tolist()
def point_distance(first: list[float], second: list[float]) -> float:
    vec1=np.array(first)
    vec2=np.array(second)
    dist=np.linlang.norm(vec1-vec2)
    return float(np.round(dist,6))
