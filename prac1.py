import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(text):
    prompt = f"""
    Summarize the following paragraph into 2-3 concise lines:

    {text}
    """

    response = model.generate_content(prompt)
    return response.text

#
paragraph = """
Artificial Intelligence is transforming industries by enabling machines to learn from data,
recognize patterns, and make decisions. It is widely used in healthcare, finance, and transportation.
AI helps automate tasks, improve efficiency, and reduce human effort while increasing accuracy.
"""


summary = summarize_text(paragraph)

print("Original Text:\n", paragraph)
print("\nSummary:\n", summary)