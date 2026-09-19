from openai import OpenAI

client = OpenAI()

def chat(user_message):
    response = client.chat.completions.create(
        model="gpt-6-astra",
        max_tokens=200,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

user_message = input("You: ")

ai_response = chat(user_message)
print(ai_response)