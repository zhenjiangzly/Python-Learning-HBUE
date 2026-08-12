# 经典算法：回文判断与字符串统计

def is_palindrome(s):
    """判断字符串是否为回文"""
    return s == s[::-1]


def count_chars(s):
    """统计每个字符出现次数"""
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def count_words(text):
    """统计英文单词数"""
    return len(text.split())


for s in ["radar", "hello", "上海自来水来自海上"]:
    print(f"{s} 是回文：{is_palindrome(s)}")

print("字符统计：", count_chars("hello world"))
print("单词数：", count_words("I love python programming"))
