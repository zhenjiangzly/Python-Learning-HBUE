# 经典算法：统计文件单词词频（TOP N）

def word_frequency(filename, top_n=5):
    """统计英文文件的词频，返回前 N 名"""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.lower().split()
    counts = {}
    for w in words:
        w = w.strip(".,!?;:'\"()")
        if w:
            counts[w] = counts.get(w, 0) + 1

    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_n], len(words)


# 生成测试文件
with open("article.txt", "w", encoding="utf-8") as f:
    f.write("Python is fun. Python is powerful. Python is easy to learn!")

top, total = word_frequency("article.txt")
print(f"总单词数：{total}")
print("词频 TOP5：")
for w, n in top:
    print(f"{w}: {n}")

import os
os.remove("article.txt")
