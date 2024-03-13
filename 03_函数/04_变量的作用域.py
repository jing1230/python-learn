# num = 10
#
# def test_01(num):
#     print(f"这个数为{num}")
#
# def test_02(num):
#     print(f"这个数为{num}")
#
# test_01(num)
# test_02(num)
# print(num)

num = 10
def test_01():
    print(f"这个数为{num}")


def test_02():
    global num  # global可以让在函数内定义的变量，成为全局变量
    num = 20
    print(f"这个数为{num}")

test_01()
test_02()
print(num)