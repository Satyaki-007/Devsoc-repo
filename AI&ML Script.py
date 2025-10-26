import requests # type: ignore
import os

input_filename = 'text.txt'
api_key = os.environ.get("Google_gemini_apikey")

with open(input_filename, 'r') as text_file:


    prompt_text = text_file.read().strip()

model_name = "gemini-pro"
endpoint_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


headers = {
    'Content-Type' : 'application/json',
    'x-goog-api-key' : api_key
}

data_to_send  = {
    "contents" : [
        {
            "parts" : [
                {"text" : prompt_text}
            ]
        }
    ]
}

response = requests.post(endpoint_url, json=data_to_send, headers=headers)

api_response = response.json()

print(api_response)


