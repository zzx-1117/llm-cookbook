# 吴泽宏 + 239210324
import os
from openai import OpenAI


api_key = "sk-"

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"


def get_summary(text):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]

    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API 调用错误: {e}")
        return None


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None


def summarize_multiple_texts(file_paths):
    summaries = []
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            if summary:
                summaries.append((file_path, summary))
            else:
                print(f"无法生成文件 '{file_path}' 的摘要。")
        else:
            print(f"无法读取文件 '{file_path}'。")
    return summaries


# 测试从多个文件读取文本并生成摘要
file_paths = [
    r"D:\239210324吴泽宏\example.txt.txt",
    r"D:\239210324吴泽宏\example1.txt.txt",
    r"D:\239210324吴泽宏\example2.txt.txt"
]

summaries = summarize_multiple_texts(file_paths)
for file_path, summary in summaries:
    print(f"文件 '{file_path}' 的摘要:")
    print(summary)
    print("-" * 40)
