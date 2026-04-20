import google.generativeai as genai

genai.configure(api_key="AIzaSyB8g8bFeseQ0-0-v2q4tBh33e1T8nxr-Xk")
model = genai.GenerativeModel("gemini-2.5-flash")

text = input("Enter sentence: ")
prompt = f"Extract important keywords from this text. Output them separated by commas: '{text}'"
response = model.generate_content(prompt)
print("\nKeywords:\n", response.text.strip())
