import os
import json
import requests
import subprocess

def call_api(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    return response.json()

def generate_summary(api_key, engine_url, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "code-davinci-002",
        "prompt": prompt,
        "max_tokens": 150
    }
    return call_api(engine_url, headers, payload)

def get_git_diff():
    try:
        diff = subprocess.check_output(['git', 'diff', 'HEAD^', 'HEAD'], text=True)
    except subprocess.CalledProcessError:
        diff = "No previous commit to compare."
    return diff

def main():
    diff = get_git_diff()
    prompt = f"Summarize the following code changes in a detailed and formatted manner:\n{diff}"

    openai_summary = generate_summary(
        os.getenv('OPENAI_API_KEY'),
        "https://api.openai.com/v1/completions",
        prompt
    )["choices"][0]["text"]

    # Assuming anthropic_summary setup remains the same
    # Include similar error handling and model updating for Anthropic API as needed

    formatted_content = f"## OpenAI Summary\n{openai_summary}\n\n## Further details to be added as required."
    print(f"::set-output name=pr_content::{json.dumps(formatted_content)}")

if __name__ == "__main__":
    main()
