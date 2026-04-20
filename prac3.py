import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

text = input("Enter text: ")
prompt = f"Classify the sentiment of the following text as Positive, Negative, or Neutral. Text: '{text}'"
response = model.generate_content(prompt)
print("\nSentiment:", response.text.strip())
