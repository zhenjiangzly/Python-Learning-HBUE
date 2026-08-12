# 第七章示例：time 库
# 时间获取、格式化、计时

import time

print("=== 时间获取 ===")
print("time.time() 时间戳：", time.time())
print("time.ctime()：", time.ctime())

print("\n=== 时间元组 ===")
t = time.localtime()
print("localtime()：", t)
print("年份：", t.tm_year)
print("月份：", t.tm_mon)
print("日期：", t.tm_mday)

print("\n=== strftime 格式化（必考） ===")
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", t))
print(time.strftime("%A", t))      # 星期
print(time.strftime("%B", t))      # 月份全称

print("\n=== strptime 解析字符串 ===")
t2 = time.strptime("2026-08-12", "%Y-%m-%d")
print("解析结果：", t2)

print("\n=== 计时 ===")
start = time.perf_counter()
time.sleep(1)                      # 暂停 1 秒
end = time.perf_counter()
print(f"耗时：{end - start:.3f} 秒")
