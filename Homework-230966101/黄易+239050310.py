#黄易239050310
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
GitHub是一个以你的工作方式为灵感的开发平台。
从开源到商业，您可以托管和审查代码，管理项目，并与5000万开发人员一起构建软件。
GitHub 是一个面向开源及私有软件项目的托管平台，因为只支持 Git 作为唯一的版本库格式进行托管，故名 GitHub。
全球1亿仓库，全球5000万开发者，全球290万家企业和组织。GitHub的用户与世界上最大的开源社区一起创建并维护有影响力的技术。
开发人员将GitHub用于个人项目，从试验新的编程语言到托管他们毕生的工作。各种规模的企业都使用GitHub来支持他们的开发过程，并安全地构建软件。
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
