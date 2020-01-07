def print_line(char, times):
    """"打印多行分隔线"""
    print(char*times)


def print_lines(char, times, n):
    """打印多行分隔线
    :param char: 使用的分割字符
    :param times: 次数
    :param n: 行数
    """
    while n>0:
        print_line(char, 50)
        n = n-1


print_lines("-", 40, 5)