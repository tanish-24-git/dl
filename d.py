import base64
encoded_string = "QUl6YVN5QjhnOGJGZXNlUTAtMC12MnE0dEJoMzNlMVQ4bnhyLVhr"
decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
decoded_string = decoded_bytes.decode('utf-8')
print("Decode-:")
print(decoded_string)
