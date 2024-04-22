import os
import json
import requests

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
        "prompt": prompt,
        "max_tokens": 150
    }
    return call_api(engine_url, headers, payload)

def main():
    # Get code difference from the last commit
    diff = os.popen('git diff HEAD^ HEAD').read()
    prompt = f"Summarize the following code changes in a detailed and formatted manner:\n{diff}"

    # Generate summaries using both APIs
    openai_summary = generate_summary(
        os.getenv('OPENAI_API_KEY'),
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        prompt
    )["choices"][0]["text"]

    anthropic_summary = generate_summary(
        os.getenv('ANTHROPIC_API_KEY'),
        "https://api.anthropic.com/claude-3/text-completions",
        prompt
    )["completions"][0]["text"]

    # Combine the results
    formatted_content = f"## OpenAI Summary\n{openai_summary}\n\n## Anthropic Summary\n{anthropic_summary}"
    print(f"::set-output name=pr_content::{json.dumps(formatted_content)}")

if __name__ == "__main__":
    main()
