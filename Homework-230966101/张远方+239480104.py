#张远方+239480104

import os
from openai import OpenAI

client = OpenAI(
    api_key="KEY",  
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
        return f"错误：API调用失败 - {e}"

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

def summarize_multiple_texts(texts):
    summaries = []
    for text in texts:
        summary = get_summary(text)
        summaries.append(summary)
    return summaries

# 测试函数
sample_text = """
人工智能（AI）是计算机科学的一个分支，旨在创建能够执行通常需要人类智能的任务的系统。这些任务包括学习、推理、问题解决、感知和语言理解。AI 系统通常基于大量数据进行训练，并使用算法来分析和解释这些数据，从而做出决策或执行任务。
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# 从文件读取文本
file_path = r" .............."
file_text = read_text_from_file(file_path)
if file_text:
    file_summary = get_summary(file_text)
    print("File Summary:", file_summary)

# 总结多个文本
texts = [
    "Text 1: 人工智能是计算机科学的一个分支。"
    "Text 2: 人工智能系统用于执行通常需要人类智能的任务。"
    "Text 3: 一些人工智能应用的例子包括语音识别和图像处理"
      
]

summaries = summarize_multiple_texts(texts)
for i, summary in enumerate(summaries):
    print(f"Summary {i+1}:", summary)
