import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://your-app-domain.com",
        "X-Title": "MailMate AI Assistant",   
    }
)

def generate_email_response(email_text, tone):
    prompt = f"""
    You are an AI assistant. Write the reply to the following email using a {tone.lower()} tone:

    Email:
    {email_text}

    Reply:
    """
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free", ## Or (qwen/qwen3-235b-a22b-07-25:free)
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

