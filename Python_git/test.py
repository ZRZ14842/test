def sum_range():
    try:
        start = int(input("请输入起始数字："))
        end = int(input("请输入结束数字："))
    except ValueError:
        return "输入的不是数字，请重试"

    if start > end:
        return "起始数字不能大于结束数字，请重试"

    total = 0
    for i in range(start, end + 1):
        total += i
    return total

print(sum_range())