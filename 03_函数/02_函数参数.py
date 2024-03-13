# def add(x, y, z):
#     print(f"{x}+{y}+{z}={x+y+z}")
#
# add(1,3,5)

import random
def check(temp):
    if temp <= 37.5:
        print(f"您的体温为{temp}度，体温正常请进！")
    else:
        print(f"体温测量中，您的体温为{temp}度，需要隔离")


print("欢迎来到黑马程序员！")


number = float(random.randint(350,450))/10
check(number)