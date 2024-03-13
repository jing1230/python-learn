str1 = "itheima"
str2 = "itcast"
str3 = "python"
num = len(str1)
print(f"str1有{num}个字母")
# count = 0
# for i in str1:
#     count += 1
# print(count)

# 函数

def my_len(data):
    number = 0
    for i in data:
        number += 1
    print(f"{data}的长度是：{number}")

my_len(str1)
my_len(str2)
my_len(str3)

# 函数的定义
'''
def 函数名（传入参数）
函数体
return 返回值
'''

# 定义
def say_hi():
    print("Hi，我是软件工程师")

# 调用
say_hi()

# 查核酸
def check_hesuan():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码以及72小时核酸证明")

check_hesuan()

