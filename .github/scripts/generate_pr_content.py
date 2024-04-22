import os
import json
import requests
import subprocess


def setup_git():
    # Set up Git by fetching all branches and tags
    subprocess.run(['git', 'fetch', '--unshallow', '--tags', '--force'], check=True)
    subprocess.run(['git', 'fetch', 'origin', '+refs/heads/*:refs/remotes/origin/*'], check=True)

def get_pr_diff():
    base_branch = os.getenv('GITHUB_BASE_REF', 'main')
    current_branch = os.getenv('GITHUB_HEAD_REF', 'main')
    try:
        # Checkout the base branch
        subprocess.run(['git', 'checkout', f'origin/{base_branch}'], check=True)
        # Get diff between base and current PR branch
        diff = subprocess.check_output(['git', 'diff', f'origin/{base_branch}', f'origin/{current_branch}'], text=True)
    except subprocess.CalledProcessError:
        diff = "Error fetching diff or no changes to compare."
    return diff

def call_api(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    return response.json()

def generate_summary(api_key, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.5
    }
    engine_url = "https://api.openai.com/v1/completions"
    return call_api(engine_url, headers, payload)

def main():
    setup_git()
    diff = get_pr_diff()
    prompt = f"Please summarize and analyze the following code changes:\n{diff}"

    openai_summary = generate_summary(
        os.getenv('OPENAI_API_KEY'),
        prompt
    )["choices"][0]["text"]

    print("Summary Generated Successfully: ", openai_summary)
    # Print to output for GitHub Actions to use
    print(f"::set-output name=pr_content::{json.dumps(openai_summary)}")

if __name__ == "__main__":
    main()

