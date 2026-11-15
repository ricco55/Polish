import ollama

mode = input("What mode would you like: ")
if mode.lower() == "professional":
    instruction = "Rewrite this message to my manager in one sentence to sound more professional. No explanations. Do not add any new information."
elif mode.lower() == "shorter":
    instruction = "Rewrite this message to my manager in one sentence. Make it as short as possible. Keep the same meaning. No explanations. Do not add any new information."
elif mode.lower() == "friendlier":
    instruction = "Rewrite this message to my manager in one sentence to sound friendlier. No explanations. Do not add any new information."
else:
    print("This mode doesn't exist we'll use the professional mode")
    instruction = "Rewrite this message to my manager in one sentence to sound more professional. No explanations. Do not add any new information."

while True:
    sentence = input("Your sentence: ")
    if sentence.lower() == "quit":
        break
    prompt = instruction + " Message: " + sentence
    response = ollama.chat(
        model="qwen3.5:4b",
        messages=[{"role": "user", "content": prompt}],
        think=False,
    )
    print(response.message.content)