import ollama

def get_instruction(mode):
    if mode.lower() == "professional":
        return "Rewrite this message to my manager in one sentence to sound more professional. No explanations. Do not add any new information."
    elif mode.lower() == "shorter":
        return "Rewrite this message to my manager in one sentence. Make it as short as possible. Keep the same meaning. No explanations. Do not add any new information."
    elif mode.lower() == "friendlier":
        return "Rewrite this message to my manager in one sentence to sound friendlier. No explanations. Do not add any new information."
    else:
        print("This mode doesn't exist we'll use the professional mode")
        return "Rewrite this message to my manager in one sentence to sound more professional. No explanations. Do not add any new information."

mode = input("What mode would you like: ")
instruction = get_instruction(mode)

while True:
    sentence = input("Your sentence: ")
    if sentence.lower() == "quit":
        break
    if sentence.lower() == "mode":
        mode = input("What mode would you like: ")
        instruction = get_instruction(mode)
        continue

    prompt = instruction + " Message: " + sentence
    response = ollama.chat(
        model="qwen3.5:4b",
        messages=[{"role": "user", "content": prompt}],
        think=False,
    )
    print(response.message.content)