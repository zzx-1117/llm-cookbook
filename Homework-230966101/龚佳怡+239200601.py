# 龚佳怡 + 239200601
import os
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",  # 提交时删除你的key，避免泄露
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
        print(f"API调用错误: {e}")
        return None

# 从文件读取文本
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

# 批量总结文本
def summarize_multiple_texts(file_paths):
    summaries = {}
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            summaries[file_path] = summary
    return summaries

# 测试函数
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# 示例：从多个文件中总结文本
file_paths = ["text1.txt", "text2.txt"]  # 替换为实际文件路径
summaries = summarize_multiple_texts(file_paths)
for path, summary in summaries.items():
    print(f"文件: {path}, 摘要: {summary}")
