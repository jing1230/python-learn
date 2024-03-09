name = "黑马程序员"
message = "学IT来：%s" % name
print(message)

setup_year = 2006
stock_price = 19.9
message = "%s,成立于 %s年,股价%.2f" % (name, setup_year, stock_price)
print(message)



# f{占位}
print(f"我是{name},成立于：{setup_year}, 我今天的股价{stock_price}")


