import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

# Read the Gemini API key from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY is not set in the environment variables.")

# API URL for Gemini (replace with actual Gemini endpoint)
engine_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Headers with Authorization token
headers = {
    'Authorization': f'Bearer {GEMINI_API_KEY}',
    'Content-Type': 'application/json'
}

# Prepare the payload for the API request
payload = {
    "contents": [
        {
            "parts": [{"text": "Write a summary for the changes made in this pull request."}]
        }
    ]
}

# Make the request to the Gemini API
response = requests.post(engine_url, headers=headers, json=payload)

# Check for successful response
if response.status_code == 200:
    response_data = response.json()
    pr_content = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    print("Generated PR Content: ", pr_content)
else:
    print(f"API request failed with status {response.status_code}: {response.text}")


# --
# import os
# import json
# import requests
# from dotenv import load_dotenv
# load_dotenv()

# # Environment variable for your Gemini API Key
# API_KEY = os.getenv("GEMINI_API_KEY")

# if not API_KEY:
#     raise Exception("GEMINI_API_KEY is not set in the environment variables.")

# # API URL for Gemini (replace with the correct endpoint for your usage)
# engine_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# # Headers
# headers = {
#     'Content-Type': 'application/json'
# }

# # Prepare the payload for the API request
# payload = {
#     "contents": [
#         {
#             "parts": [{"text": "Write a story about a magic backpack."}]
#         }
#     ]
# }

# # Make the request to the Gemini API
# response = requests.post(engine_url, headers=headers, json=payload)

# # Check for a successful response
# if response.status_code == 200:
#     print("Response from Gemini API:")
#     print(response.json())
# else:
#     print(f"API request failed with status {response.status_code}: {response.text}")

# --
