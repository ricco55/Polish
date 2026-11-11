import ollama

sentence = input("Your sentence: ")

prompt = "Rewrite this message to my manager in one sentence to sound more professional. No explanations. Do not add any new information. Message: " + sentence

response = ollama.chat(
    model="qwen3.5:4b",
    messages=[{"role": "user", "content": prompt}],
    think=False,
)

print(response.message.content)