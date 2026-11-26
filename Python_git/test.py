def sum_1_to_n():
    user_input = input("请输入一个数字：")
    try:
        n = int(user_input)
    except ValueError:
        return "输入的不是一个数字，请重试"
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

while True:
    print(sum_1_to_n())