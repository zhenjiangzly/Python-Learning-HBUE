# 第七章示例：jieba 中文分词
# 需要先安装：pip install jieba

import jieba

text = "湖北经济学院位于武汉，是一所省属本科高校"

print("=== 精确模式（最常用） ===")
words = jieba.lcut(text)
print(words)

print("\n=== 全模式 ===")
print(jieba.lcut(text, cut_all=True))

print("\n=== 搜索引擎模式 ===")
print(jieba.lcut_for_search(text))

print("\n=== 词频统计 ===")
counts = {}
for w in jieba.lcut(text):
    if len(w) > 1:      # 排除单字
        counts[w] = counts.get(w, 0) + 1
for w, n in counts.items():
    print(f"{w}: {n}")
