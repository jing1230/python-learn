# # 演示for循环的基础语法
# name = "itheima"
# for x in name: # for 变量 in 被处理的数据
#     # 将name的内容，逐个取出赋予x临时变量
#     # 就可以在循环体内对x进行处理
#     print(x)

i = 0
num = 0
lesson = input()
for x in lesson:
    i += 1
    if x == "a" :
        num += 1
print(f"共有{i}个字母，{num}个a")