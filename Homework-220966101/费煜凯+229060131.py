import os
from openai import OpenAI
import json
import time  # 用于实现重试机制

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

# 用于调用API生成摘要
def get_summary(text):
    prompt = f"总结以下文本内容，限制在3-5句话：\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    
    try:
        # 增加API调用的重试机制
        for _ in range(3):  # 尝试3次
            try:
                response = client.chat.completions.create(
                    model=deployment,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=150
                )
                return response.choices[0].message.content
            except Exception as api_error:
                print(f"API 调用失败，重试中... 错误信息: {str(api_error)}")
                time.sleep(2)  # 等待2秒后重试
        print("多次尝试后仍然无法获取摘要。")
        return None
    except Exception as e:
        print(f"处理 API 请求时出错: {str(e)}")
        return None

# 从文件中读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 找不到。")
        return None
    except Exception as e:
        print(f"读取文件 '{file_path}' 时出错: {str(e)}")
        return None

# 对多个文本进行总结
def summarize_multiple_texts(file_paths):
    summaries = {}
    
    for file_path in file_paths:
        print(f"正在处理文件: {file_path}")
        text = read_text_from_file(file_path)
        
        if text:
            summary = get_summary(text)
            if summary:
                summaries[file_path] = summary
            else:
                summaries[file_path] = "无法生成摘要。"
        else:
            summaries[file_path] = "无法读取文本。"

    return summaries


file_paths = ["file1.txt", "file2.txt", "file3.txt"]
summaries = summarize_multiple_texts(file_paths)

for file, summary in summaries.items():
    print(f"{file} 的摘要:\n{summary}\n")

output_file = "summaries.json"
try:
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(summaries, json_file, ensure_ascii=False, indent=4)
        print(f"摘要已保存到 {output_file}")
except Exception as e:
    print(f"保存摘要到文件时出错: {str(e)}")
