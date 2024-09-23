import os
from openai import OpenAI

client = OpenAI(
  api_key="",
  base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content

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
# TODO: Implement error handling for API calls
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
    
    except client.error.OpenAIError as e:
        print(f"OpenAI API error occurred: {str(e)}")
        return None
    
    except client.error.AuthenticationError:
        print("Authentication failed: Check your API key and credentials.")
        return None
    
    except client.error.RateLimitError:
        print("Rate limit exceeded: Too many requests made. Please try again later.")
        return None
    
    except client.error.ServiceUnavailableError:
        print("Service is temporarily unavailable. Please try again later.")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

# TODO: Add functionality to summarize multiple texts
def summarize_multiple_texts(texts):
    summaries = []
    for i, text in enumerate(texts):
        print(f"Summarizing text {i + 1} out of {len(texts)}...")
        summary = get_summary(text)
        if summary:
            summaries.append(summary)
        else:
            summaries.append(f"Summary for text {i + 1} could not be generated.")
    return summaries

