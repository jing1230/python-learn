import random
count = 10000
staff = 20
for i in range(staff) :
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效{num},低于5，不发工资，下一位")
    else:
        count = count - 1000
        if count >= 0:
            print(f"员工{i}发放工资1000元，账户余额{count}元")
        else:
            print("工资发完了，下个月再领取吧")
            break




