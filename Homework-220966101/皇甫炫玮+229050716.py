import os
import time
import logging
import openai
from openai import OpenAI

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

client = OpenAI(
    api_key="",  # 提交时删除你的key，避免泄露
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

# 从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        logging.error(f"错误：无法读取文件 '{file_path}'。")
    return None

# 获取摘要的函数
def get_summary(text, retries):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=deployment,
                messages=messages,
                temperature=0.7,
                max_tokens=100
            )
            return response.choices[0].message.content
        
        except (openai.APIConnectionError, openai.RateLimitError) as api_err:
            logging.warning(f"API调用失败: {api_err}. 尝试第 {attempt + 1} 次重试...")
            time.sleep(2)  # 等待 2 秒后重试
        except Exception as e:
            logging.error(f"未知错误: {e}")
            return None
    
    logging.error("所有方案失效。")
    return None

# 处理多个文件的摘要
def summarize_multiple_texts(file_paths):
    summaries = {}
    
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text is not None:
            summary = get_summary(text, 3)
            if summary:
                summaries[file_path] = summary
            else:
                summaries[file_path] = "没有摘要！"
        else:
            summaries[file_path] = "文本读取失败！"
    
    return summaries

# 测试
sample_text = """
[突然，一只寄居蟹悄悄探出头，成了城堡的第一位居民。小男孩惊喜地笑了，与海浪和寄居蟹共享这份简单的快乐.]
"""

summary = get_summary(sample_text,3)
print("Summary:", summary)   
# 测试
file_paths = ["test1.txt", "test2.txt"]
summaries = summarize_multiple_texts(file_paths)
print("摘要:", summaries)
