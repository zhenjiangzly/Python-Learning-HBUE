# 经典算法：矩阵（二维列表）操作

def matrix_sum(m):
    """矩阵所有元素之和"""
    return sum(sum(row) for row in m)


def matrix_transpose(m):
    """矩阵转置"""
    return [list(row) for row in zip(*m)]


def row_sums(m):
    """每行之和"""
    return [sum(row) for row in m]


def col_sums(m):
    """每列之和"""
    n = len(m)
    return [sum(m[i][j] for i in range(n)) for j in range(n)]


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("矩阵：", m)
print("元素总和：", matrix_sum(m))
print("每行之和：", row_sums(m))
print("每列之和：", col_sums(m))
print("转置：", matrix_transpose(m))
