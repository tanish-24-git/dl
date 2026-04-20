import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

product = input("Enter product: ")
audience = input("Enter target audience: ")
price = input("Enter price: ")

prompt = f"Create a catchy, persuasive advertisement. Product name: {product}, Target audience: {audience}, Price: {price}"
response = model.generate_content(prompt)
print("\nAdvertisement:\n\n", response.text.strip())
