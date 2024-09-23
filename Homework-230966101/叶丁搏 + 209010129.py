# 叶丁搏 + 209010129
import os
from openai import OpenAI

client = OpenAI(
  api_key="sk-4d3ac203670148f0972a24b79c2dcd67", # 提交时删除你的key，避免泄露
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

# Test the function
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# 实现一个从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

# 实现API调用的错误处理
def safe_get_summary(text):
    try:
        return get_summary(text)
    except Exception as e:
        print(f"API调用错误: {e}")
        return None

# 添加功能以总结多个文本
def summarize_multiple_texts(texts):
    summaries = []
    for text in texts:
        summary = safe_get_summary(text)
        if summary:
            summaries.append(summary)
    return summaries

# 示例：从文件读取文本并总结
file_path = "sample_text.txt"
text = read_text_from_file(file_path)
if text:
    summary = safe_get_summary(text)
    if summary:
        print("Summary from file:", summary)
    else:
        print("无法生成总结。")

# 示例：总结多个文本
texts = [
    "This is the first text to summarize.",
    "This is the second text to summarize.",
    "This is the third text to summarize."
]
summaries = summarize_multiple_texts(texts)
for i, summary in enumerate(summaries):
    print(f"Summary {i+1}:", summary)
