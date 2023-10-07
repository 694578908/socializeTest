from config.color import print_centered_ansi

counter = 0


# 定义计数器
def count(data):
    global counter
    separator = '>' * 20
    counter += 1  # 递增类级别的测试用例计数器
    print_centered_ansi(f"\n{separator}执行第{counter}条用例{separator}\n", '33')
    return data
