import requests
import json

# Replace API_KEY with your actual OpenAI API key
API_KEY = "API_KEY"

# The URL of the OpenAI API endpoint
url = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

# The parameters for the API request
params = {
    "model": "text-davinci-002",
    "prompt": "Write a short story about a dragon",
    "max_tokens": 1000
}

# Add the API key to the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}

# Make the API request
response = requests.post(url, headers=headers, json=params)

# Check for a successful response
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)

    # Print the generated text
    print(data["choices"][0]["text"])
else:
    # Print the error message
    print("Error:", response.text)
