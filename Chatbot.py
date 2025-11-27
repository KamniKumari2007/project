from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

while True:
    q = input("You: ")
    if q == "exit":
        break

    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": q}]
    )

    print("Bot:", res.choices[0].message["content"])
