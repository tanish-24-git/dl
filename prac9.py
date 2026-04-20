import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

text = input("Enter sentence: ")
prompt = f"Paraphrase this sentence while preserving its original meaning: '{text}'"
response = model.generate_content(prompt)
print("\nParaphrased Sentence:\n", response.text.strip())
