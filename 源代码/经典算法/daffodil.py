# 经典算法：水仙花数与数字拆分

def split_digits(n):
    """把整数拆成各位数字（列表）"""
    return [int(d) for d in str(n)]


def is_daffodil(n):
    """三位水仙花数：各位数字的立方和等于本身"""
    digits = split_digits(n)
    return sum(d ** 3 for d in digits) == n


# 输出所有三位水仙花数
daffodils = [n for n in range(100, 1000) if is_daffodil(n)]
print("三位水仙花数：", daffodils)   # [153, 370, 371, 407]

# 数字拆分的另一种写法
n = 12345
digits = []
while n > 0:
    digits.append(n % 10)
    n //= 10
digits.reverse()
print("12345 的各位数字：", digits)
