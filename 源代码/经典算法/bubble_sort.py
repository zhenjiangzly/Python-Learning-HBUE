# 经典算法：冒泡排序
# 相邻元素两两比较，大的往后冒

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):   # 每轮末尾元素已就位
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:              # 本轮无交换，已有序
            break
    return lst


nums = [64, 34, 25, 12, 22, 11, 90]
print("排序前：", nums)
print("排序后：", bubble_sort(nums))
