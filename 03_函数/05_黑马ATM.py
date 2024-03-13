money = 5000000 # 余额
name = input("请输入客户姓名：")

def query_balance():
    print(f"账户余额：{money}")

def save(number):
    global money
    money += number
    print(f"存款{number}成功")


def withdraw(number):
    global money
    money -= number
    print(f"取款{number}成功")

def bank_menu():
    print(f"***********欢迎来到黑马ATM！************")
    print(f"1,查询余额；\t2,存钱\t3,取钱")
    num = int(input("请输入（1,2,3）:"))
    if num == 1:
        query_balance()
    elif num == 2:
        number = float(input("请输入存取金额："))
        save(number)
    elif num == 3 :
        number = float(input("请输入存取金额："))
        withdraw(number)
    else:
        exit()

while True:
    bank_menu()