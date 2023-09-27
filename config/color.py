import shutil


def print_centered_ansi(text, color_code):
    # ��ȡ�ն˵Ŀ��
    terminal_width = shutil.get_terminal_size().columns
    # ����Ҫ��ӡ���ı�����
    text_length = len(text)
    # ����������Ŀո���
    left_padding = (terminal_width - text_length) // 2
    # �����ұ����Ŀո���
    right_padding = terminal_width - text_length - left_padding
    # ������ߺ��ұߵ�����ַ���
    left_fill = " " * left_padding
    right_fill = " " * right_padding
    # �������յľ����ı�
    centered_text = f"\033[{color_code}m{left_fill}{text}{right_fill}\033[0m"
    # ��ӡ�����ı�
    print(centered_text)
