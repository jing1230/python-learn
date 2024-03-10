# # print("Hello", end=' ')
# # print("World")
#
# print("Hello World!")
# print("itheima best")
#
# # 制表符：对齐
# print("Hello\tWorld!")
# print("itheima\tbest")

# while循环打印九九乘法表
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j*i}",end="\t")
#         j += 1
#     print()
#     i += 1

# for循环打印九九乘法表
i = 1
j = 1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i * j}\t",end=" ")
    print()
