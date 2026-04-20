import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

topic = input("Enter email topic: ")
prompt = f"Write a professional email about: {topic}"
response = model.generate_content(prompt)
print("\nGenerated Email:\n\n", response.text.strip())
