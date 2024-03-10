height = int(input("Enter your height in:"))
vip = int(input("Enter your vip grade（1-5）:"))
if height <= 120:
    print("您的身高小于120，可以免费游玩！")
elif vip >= 3:
    print(f"您的vip等级大于3，可以免费游玩。")
else :
    print(f"条件不满足，您需要补票10元")

print(f"祝您游玩愉快！")