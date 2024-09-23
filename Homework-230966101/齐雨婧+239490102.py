#齐雨婧+239490102
import os
import requests
from openai import OpenAI, OpenAIError

client = OpenAI(
  api_key="",
  base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

# TODO 1: 实现从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

# TODO 2: 实现API调用的错误处理
def get_summary(text):
    try:
        prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content

    except OpenAIError as e:
        print(f"API调用失败，错误信息: {e}")
        return None
    except requests.exceptions.Timeout:
        print("请求超时，请稍后重试。")
        return None
    except requests.exceptions.ConnectionError:
        print("网络连接错误，请检查网络。")
        return None
    except Exception as e:
        print(f"发生其他错误: {e}")
        return None

# TODO 3: 增加处理多个文本摘要的功能
def summarize_multiple_texts(file_paths):
    summaries = []
    
    for path in file_paths:
        text = read_text_from_file(path)
        if text:
            print(f"正在生成文件 {path} 的摘要...")
            summary = get_summary(text)
            if summary:
                summaries.append(summary)
            else:
                summaries.append(f"文件 {path} 的摘要生成失败。"
    return summaries
        file_paths = ["file1.txt", "file2.txt", "file3.txt"]  # 替换为实际文件路径
       summaries = summarize_multiple_texts(file_paths)
for i, summary in enumerate(summaries, 1):
    print(f"文件 {i} 的摘要:")
    print(summary)
