# while循环

# i = 0;
# while i < 10:
#     print("小帅，我喜欢你")
#     i += 1


# 猜数字（有限次数）
# import random
# num = random.randint(1,10)
# # print(num)
# print(f"你有三次机会：")
# i = 0
# while i < 3:
#     guess = int(input(f"请输入："))
#     if guess == num:
#         print(f"恭喜你猜对了")
#     else:
#         print(f"猜错啦")
#     i += 1

# 猜数字（无限次数）
import random
num = random.randint(1,100)
# print(num)
count = 0 # 猜的次数
flag = True
while flag:
    count += 1
    guess = int(input("请猜数字："))
    if guess > num:
        print("猜大了")
    elif guess < num:
        print("猜小了")
    else:
        print("恭喜你猜对了")
        # 终止条件
        flag = False
print(f"你一共猜了{count}次")