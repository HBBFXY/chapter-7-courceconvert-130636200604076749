# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
# 1. 读取random_int.py文件内容
with open("random_int.py", "r", encoding="utf-8") as f:
    content = f.readlines()  # 按行读取，保留代码结构

processed_content = []
for line in content:
    # 拆分每行内容为“单词+符号”的列表（简单处理，保留代码语法结构）
    temp = []
    current_word = ""
    for char in line:
        if char.isalnum() or char == "_":  # 识别变量/关键字的字符
            current_word += char
        else:
            if current_word:
                # 判断当前单词是否为保留字，非保留字则转大写
                if current_word in reserved_words:
                    temp.append(current_word)
                else:
                    temp.append(current_word.upper())
                current_word = ""
            temp.append(char)  # 添加符号
    # 处理行末尾的单词
    if current_word:
        if current_word in reserved_words:
            temp.append(current_word)
        else:
            temp.append(current_word.upper())
    # 拼接处理后的行
    processed_line = "".join(temp)
    processed_content.append(processed_line)

# 2. 将处理后的内容保存到新文件（如converted_random_int.py）
with open("converted_random_int.py", "w", encoding="utf-8") as f:
    f.writelines(processed_content)
