import os
from openai import OpenAI
from openai.error import OpenAIError

client = OpenAI(
    api_key="your-api-key",  # 提交时删除你的 key，避免泄露
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

# 获取文本摘要
def get_summary(text):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    
    # TODO: Implement error handling for API calls
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except (OpenAIError, KeyError) as e:
        print(f"API 调用错误或响应解析失败: {e}")
        return "无法生成摘要。"

# 从文件中读取文本
def read_text_from_file(file_path):
    # 使用更简洁的上下文管理器来处理文件操作
    if not os.path.exists(file_path):
        print(f"错误：文件 '{file_path}' 不存在。")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"文件读取失败：{e}")
        return None

# TODO: Add functionality to summarize multiple texts
def summarize_multiple_texts(file_paths):
    # 通过生成器和列表推导进行文本处理
    return [
        get_summary(read_text_from_file(file)) if read_text_from_file(file) else f"文件 '{file}' 无法读取或为空。"
        for file in file_paths
    ]

# 测试多文本摘要功能
file_list = ['file1.txt', 'file2.txt', 'file3.txt']  # 替换为实际文件路径
summaries = summarize_multiple_texts(file_list)

# 输出摘要结果
for i, summary in enumerate(summaries):
    print(f"文件 {i+1} 的摘要: {summary}")
