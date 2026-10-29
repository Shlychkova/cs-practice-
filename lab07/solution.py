import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr=np.asarray(values,dtype=float)
    reshaped=arr.reshape(-1,width)
    return np.round(reshaped,6).tolist()
def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix:
        return []
    arr=np.asarray(matrix,dtype=float)
    selected_block=arr[np.ix_(rows,columns)]
    return np.round(selected_block,6).tolist()
def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr=np.asarray(matrix,dtype=float)
    means=np.mean(arr,axis=0)
    return np.round(means,6).tolist()
def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return []
    arr=np.asarray(matrix,dtype=float)
    col_data=arr[:,column]
    res=np.max(col_data)-np.min(col_data)
    return float(np.round(res,6))
