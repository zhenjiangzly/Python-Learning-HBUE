# 经典算法：二分查找
# 在有序列表中查找元素，每次排除一半

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid            # 找到，返回索引
        elif lst[mid] < target:
            low = mid + 1         # 目标在右半部分
        else:
            high = mid - 1        # 目标在左半部分
    return -1                     # 未找到


nums = [1, 3, 5, 7, 9, 11, 13, 15]
print("列表：", nums)
print("查找 7：索引", binary_search(nums, 7))
print("查找 8：索引", binary_search(nums, 8))
