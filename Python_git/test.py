def sum_1_to_n():
    n = int(input("请输入一个数字："))
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_1_to_n())