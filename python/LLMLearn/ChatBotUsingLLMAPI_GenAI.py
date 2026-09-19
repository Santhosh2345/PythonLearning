from google import genai

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash"
)

def chat_with_ai(user_message):
    response = chat.send_message(user_message)
    return response.text

while True:
    user_message = input("You: ")

    if user_message == "exit":
        break
    gen_ai_response = chat_with_ai(user_message)
    print(gen_ai_response)