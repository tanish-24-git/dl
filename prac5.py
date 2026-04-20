import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

text = input("Enter sentence: ")
prompt = f"Correct the grammar of this sentence and output only the corrected sentence: '{text}'"
response = model.generate_content(prompt)
print("\nCorrected Sentence:\n", response.text.strip())
