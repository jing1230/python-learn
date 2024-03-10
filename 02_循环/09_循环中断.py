# # continue 当前循环结束
# for i in range (1,6):
#     print("hhh")
#     continue
#     print("哈哈哈")


# for i in range(1,6):
#     print("1")
#     for j in range(1,6):
#         print("2")
#         continue
#         print("3") # 运行不到这
#     print(4)



# break 整个循环结束
for i in range(1,6):
    print("1")
    for j in range(1,6):
        print("2")
        break
        print(3)
    print("4")
print("6")