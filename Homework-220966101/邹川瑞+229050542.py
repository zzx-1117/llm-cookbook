import os
from openai import OpenAI
import json

client = OpenAI(
    api_key="your-api-key",
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
        print(f"Error during API call: {str(e)}")
        return None

# TODO 1: Implement a function to read text from a file
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        return None

# TODO 2: Implement error handling for API calls (done in the get_summary function)

# TODO 3: Add functionality to summarize multiple texts
def summarize_multiple_texts(file_paths):
    summaries = {}
    
    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        text = read_text_from_file(file_path)
        
        if text:
            summary = get_summary(text)
            if summary:
                summaries[file_path] = summary
            else:
                summaries[file_path] = "Failed to generate summary."
        else:
            summaries[file_path] = "Failed to read text."

    return summaries


file_paths = ["file1.txt", "file2.txt", "file3.txt"]  # Replace with actual file paths
summaries = summarize_multiple_texts(file_paths)


for file, summary in summaries.items():
    print(f"Summary for {file}:\n{summary}\n")
    

output_file = "summaries.json"
try:
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(summaries, json_file, ensure_ascii=False, indent=4)
        print(f"Summaries saved to {output_file}")
except Exception as e:
    print(f"Error saving summaries to file: {str(e)}")
