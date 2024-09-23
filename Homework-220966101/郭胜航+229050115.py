import os
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"


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
    # TODO Implement error handling for API calls
    except Exception as e:
        print(f"调用API时发生错误，错误信息是: {e}")

# Test the function
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)


# TODO: Implement a function to read text from a file
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None


# TODO: Add functionality to summarize multiple texts
file_paths = ["/a.txt","/b.txt","/c.txt"]
def summarize_texts(file_paths):
    summaries = {}
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            summary = get_summary(text)
        summaries[file_path] = summary
    return summaries
