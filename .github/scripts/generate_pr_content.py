import os
import requests
import subprocess


def call_api(url, headers, payload):
    """Helper function to make the API request."""
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(
            f"API request failed with status {response.status_code}: {response.text}"
        )
    return response.json()


def generate_summary(api_provider, api_key, engine_url, prompt):
    """Generates a PR summary using OpenAI or Gemini API."""
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    if api_provider == "openai":
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 150,
            "temperature": 0.7,
        }
    elif api_provider == "gemini":
        payload = {
            "model": "gemini-1.5-pro-latest",
            "prompt": prompt,
            "max_tokens": 300,
            "temperature": 0.7,
        }
    else:
        raise ValueError(f"Unsupported API provider: {api_provider}")

    return call_api(engine_url, headers, payload)


def get_git_diff():
    """Fetches the git diff between the current and previous commit."""
    try:
        diff = subprocess.check_output(["git", "diff", "HEAD^", "HEAD"], text=True)
    except subprocess.CalledProcessError:
        diff = subprocess.check_output(["git", "diff", "HEAD"], text=True)
    return diff


def main():
    diff = get_git_diff()
    print("Generated Git Diff:\n", diff)
    prompt = f"Summarize the following code changes:\n{diff}"

    api_provider = os.getenv("API_PROVIDER", "openai").lower()

    if api_provider == "openai":
        engine_url = "https://api.openai.com/v1/chat/completions"
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key is missing!")
        summary = generate_summary(api_provider, api_key, engine_url, prompt)[
            "choices"
        ][0]["message"]["content"]

    elif api_provider == "gemini":
        engine_url = "https://api.gemini.com/v1/generate"
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini API key is missing!")
        summary = generate_summary(api_provider, api_key, engine_url, prompt)[
            "choices"
        ][0]["text"]

    else:
        raise ValueError(f"Unsupported API provider: {api_provider}")

    formatted_content = f"## {api_provider.capitalize()} Summary\n{summary}\n\n## Further details to be added as required."
    print(formatted_content)


if __name__ == "__main__":
    main()
