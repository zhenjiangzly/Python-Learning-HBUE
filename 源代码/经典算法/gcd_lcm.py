# 经典算法：最大公约数（辗转相除法）与最小公倍数

def gcd(a, b):
    """辗转相除法求最大公约数"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """最小公倍数 = 两数之积 / 最大公约数"""
    return a * b // gcd(a, b)


print("gcd(24, 36) =", gcd(24, 36))   # 12
print("gcd(17, 13) =", gcd(17, 13))   # 1（互质）
print("lcm(4, 6) =", lcm(4, 6))       # 12
