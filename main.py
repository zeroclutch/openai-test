import openai
 # from dotenv import load_dotenv
import json

# load_dotenv()

openai.api_key = "YOUR_API_KEY_HERE"

# Ask OpenAI
def ask_openai(user_prompt):
    response = openai.Completion.create(
        engine="text-ada-001", # Cheapest engine
        prompt=user_prompt,    # Populate with content from POST request
        temperature=0.1,       # Creativity
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    return response

# Triggered every get request
def handler(request):
    user_prompt = str(request.get_data())
    result = ask_openai(user_prompt)
    print(user_prompt)
    # Send this to the ser
    return result
