# 经典算法：素数判断与素数筛选

def is_prime(n):
    """判断 n 是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # 只需检查到 sqrt(n)
        if n % i == 0:
            return False
    return True


def primes_below(n):
    """输出 n 以内的所有素数"""
    return [x for x in range(2, n + 1) if is_prime(x)]


for n in [2, 3, 9, 17, 97]:
    print(f"{n} 是素数：{is_prime(n)}")

print("100 以内的素数：", primes_below(100))
