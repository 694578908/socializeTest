from bs4 import BeautifulSoup
import os


class HTMLReportCleaner:

    def __init__(self, file_path='./reports/report.html'):
        self.file_path = file_path

    def clean_old_report(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"旧的 HTML 报告文件 '{self.file_path}' 已被清理。")
        else:
            print(f"未找到 HTML 报告文件 '{self.file_path}'，无需清理。")


class HTMLModifier:
    def __init__(self, file_path='./reports/report.html'):
        self.file_path = file_path

    def modify_html_content(self, append_values, edit_values):
        # 读取 HTML 文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # 使用 Beautiful Soup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        # 获取要追加内容的标签名称和内容
        for append_tag_name, find_text, append_tag_content in filter(None, append_values):

            append_tag = soup.find(append_tag_name, string=find_text)

            # 如果找到标签，向其内容添加新值
            if append_tag:
                append_tag.append(append_tag_content)
            else:
                print(f"标签 '{append_tag_name}' 中的内容 '{find_text}' 未在 HTML 中找到。")
        # 遍历传递的标签名和新值的字典
        for edit_name, edit_text, new_value in filter(None, edit_values):

            # 查找指定的 HTML 标签
            tag = soup.find(edit_name, string=edit_text)

            # 如果找到标签，修改标签的文本内容
            if tag:
                tag.string = new_value
            else:
                print(f"Tag '{edit_name}' not found in the HTML.")

        # 将修改后的 HTML 内容写回文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

    def edit_html(self):
        # 添加
        append_values = [()]
        # 修改
        edit_values = [('h2', 'Summary', '总结'),
                       ('h1', 'report.html', '接口自动化测试用例报告'),
                       ('h2', 'Results', '结果>>>社交用户端接口自动化Allure测试报告访问地址: https://dada-codetest-member.qyfriend.com')]
        self.modify_html_content(append_values, edit_values)
