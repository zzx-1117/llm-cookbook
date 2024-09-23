# 叶丁搏 + 209010129
import os
from openai import OpenAI

client = OpenAI(
  api_key=" ", # 提交时删除你的key，避免泄露
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
"在一个宁静的小镇上，有一位名叫艾米莉的年轻女孩。她总是对星空充满了好奇。每个夜晚，她都坐在窗边，仰望着那片无垠的星海，梦想有一天能探索宇宙的奥秘。
有一天，艾米莉在镇上的旧书店里发现了一本关于天文学的书。书中详细描述了星座、行星和银河系的奇妙。她如获至宝，开始认真学习书中的知识。"

"随着时间的推移，艾米莉的热情感染了她的朋友们。她组织了一次星空观测活动，邀请大家一起用她的望远镜观察夜空。那晚，星星格外明亮，大家都被宇宙的美丽所震撼。
从那以后，艾米莉和她的朋友们成立了一个天文俱乐部，定期分享他们的发现和心得。小镇也因此变得更加充满活力和好奇心。"

"艾米莉的故事告诉我们，追随自己的热情，不仅能点亮自己的生活，也能照亮他人的世界。"
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
file_path = r"E:\stage 5\软件工程实践2\llm-cookbook-main\llm-cookbook-main\content\1.txt"
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
