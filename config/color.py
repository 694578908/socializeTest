import shutil


def print_centered_ansi(text, color_code):
    # 获取终端的宽度
    terminal_width = shutil.get_terminal_size().columns
    # 计算要打印的文本长度
    text_length = len(text)
    # 计算左边填充的空格数
    left_padding = (terminal_width - text_length) // 2
    # 计算右边填充的空格数
    right_padding = terminal_width - text_length - left_padding
    # 生成左边和右边的填充字符串
    left_fill = " " * left_padding
    right_fill = " " * right_padding
    # 生成最终的居中文本
    centered_text = f"\033[{color_code}m{left_fill}{text}{right_fill}\033[0m"
    # 打印居中文本
    print(centered_text)


# 红色字体并加粗
def colorize_text(text, style='\033[1m\033[31m'):
    end_style = '\033[0m'
    return style + text + end_style
