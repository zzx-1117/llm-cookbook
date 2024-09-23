# 鲍奕铭239480406
import os
from openai import OpenAI

client = OpenAI(
  api_key="",
  base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat" 
  def get_summary(text):
    print("我在思考...")
    try:
        prompt = f"Summarize the following text in 1 sentences:\n\n{text}"
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        # TODO Implement error handling for API calls
        # 处理API调用时可能会出现的异常
        print(f"调用API时发生错误，错误信息是: {e}")

# Test the function
sample_text = """
近日，有网友发视频称，拥有千万粉丝的鉴宝网红“听泉鉴宝”连线一名网友时，该网友展示了多件“国宝级文物”，并称其中的一把“巴剑”是“从博物馆拿出来的”。
9月22日，封面新闻分别联系到夔州博物馆和重庆奉节县文旅委，两家单位的工作人员表示，文物不可能从博物馆里拿走；当地多个部门正在就相关情况进行核查。
"""
summary = get_summary(sample_text)
print("Summary:", summary)
  # TODO: Add functionality to summarize multiple texts
def summarize_texts(file_paths):
    # 为每个文本都生成自己的摘要信息
    summaries = {}
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text is not None:
            summary = get_summary(text)
            if summary:
                summaries[file_path] = summary
            else:
                summaries[file_path] = "没有摘要！"
        else:
            summaries[file_path] = "文本读取失败！"
    return summaries

# 多个txt的路径列表
file_paths = [
    "C:/Users/YourUsername/Documents/file1.txt",
    "C:/Users/YourUsername/Documents/file2.txt",
    "C:/Users/YourUsername/Documents/file3.txt"]
summaries = summarize_texts(file_paths)

# 输出每个txt的摘要
for file_path, summary in summaries.items():
    print(f"{file_path} 的摘要是: {summary}")
