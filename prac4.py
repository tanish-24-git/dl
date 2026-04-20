import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

text = input("Enter English text: ")
prompt = f"Translate this text to Hindi: '{text}'"
response = model.generate_content(prompt)
print("\nHindi Translation:\n", response.text.strip())
