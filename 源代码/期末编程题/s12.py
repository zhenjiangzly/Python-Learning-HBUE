# 7-12 字典查询电话号码
phone_book = {"张小红": "15013767368", "李四": "15262356789",
              "胡旭": "15897653123", "王梅": "156325879411",
              "孙兴": "15248936126"}
name = input()
if name in phone_book:
    print(f"{name}的电话是{phone_book[name]}")
else:
    print("查无此人")
