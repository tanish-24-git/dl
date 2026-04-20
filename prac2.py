import google.generativeai as genai

genai.configure(api_key="") 
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()

print("Type 'exit' to stop")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break
    response = chat.send_message(user_input)
    print("Bot:", response.text)
