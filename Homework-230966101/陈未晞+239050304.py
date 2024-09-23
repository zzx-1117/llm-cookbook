#陈未晞+239050304
import os
from openai import OpenAI

client = OpenAI(
  api_key="456123456123", # 提交时删除你的key，避免泄露
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
        print(f"错误：API 调用失败 - {e}")
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

def summarize_multiple_texts(texts):
    combined_text = " ".join(texts)
    return get_summary(combined_text)

# 测试从文件读取文本
file_path = "sample_text.txt"
text = read_text_from_file(file_path)
if text:
    print("从文件读取的文本：", text)

# 测试汇总多个文本
texts = [
    "自然语言处理（NLP）是人工智能的一个子领域，专注于使计算机能够理解和生成人类语言。",
    "NLP 技术广泛应用于机器翻译、情感分析、文本摘要和问答系统等领域。",
    "近年来，随着深度学习的发展，NLP 取得了显著的进展，尤其是在预训练语言模型方面。"
]

summary = summarize_multiple_texts(texts)
if summary:
    print("Summary:", summary)
