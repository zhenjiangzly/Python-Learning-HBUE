# 经典算法：选择排序
# 每轮选择最小的元素放到前面

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):    # 找 i 之后的最小值
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]   # 交换到位置 i
    return lst


nums = [64, 25, 12, 22, 11]
print("排序前：", nums)
print("排序后：", selection_sort(nums))
