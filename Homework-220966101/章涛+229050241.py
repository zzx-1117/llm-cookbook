import os
from openai import OpenAI
from openai.error import OpenAIError, AuthenticationError, APIError

client = OpenAI(
    api_key="your-api-key",  # 提交时删除你的key，避免泄露
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

# 实现汇总功能的函数
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
    except AuthenticationError:
        return "API身份验证失败。请检查你的API密钥。"
    except APIError as e:
        return f"API调用失败。错误信息: {str(e)}"
    except OpenAIError as e:
        return f"调用时发生未预料的错误: {str(e)}"
    except Exception as e:
        return f"发生了一个一般性错误: {str(e)}"

# 从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

# 实现汇总多段文本的功能
def summarize_multiple_texts(file_paths):
    summaries = []
    
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            summaries.append(summary)
        else:
            print(f"跳过文件 '{file_path}'，因为无法读取其内容。")
    
    return summaries

# 测试
file_paths = ["text1.txt", "text2.txt"]  # 将这些文件替换为实际存在的文本文件路径
summaries = summarize_multiple_texts(file_paths)

for i, summary in enumerate(summaries, start=1):
    print(f"Summary {i}:", summary)
