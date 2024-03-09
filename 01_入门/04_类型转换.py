# 将数字类型转换成字符串 str()
num_str = str(11)
print(type(num_str), num_str)

# 将字符串转换为数字
num = int("111")
print(type(num), num)

# # 错误示范，()字符串里面内容必须是数字，才能转换
# num1 = int("a")
# print(type(num1), num1)

num2 = int(111.1)
print(type(num2), num2)