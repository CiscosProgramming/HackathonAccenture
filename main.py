from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts
import random
import os

# Load environment variables
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Model config
model = "gpt-3.5-turbo"
temperature = 0.7
max_tokens = 500

# Start with a random childhood question
initial_question = random.choice(prompts.CHILDHOOD_QUESTIONS)
print(f"AI: {initial_question}")

# Initialize message history
messages = [
    prompts.SYSTEM_MESSAGE,
    {"role": "assistant", "content": initial_question}
]

# Start chat loop
while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Append user response
    messages.append({"role": "user", "content": user_input})

    # Let the AI both respond and generate the next question
    assistant_prompt = (
    "Responde de forma calorosa à última mensagem do utilizador em português de Portugal. "
    "O teu objetivo é estimular a memória de um utilizador idoso. "
    "Podes fazer perguntas sobre a sua infância, juventude ou momentos marcantes da vida. "
    "Se for apropriado, também podes sugerir pequenos jogos de palavras, adivinhas, ou perguntas divertidas que o façam pensar ou sorrir. "
    "Mantém um tom calmo, respeitoso e encorajador."
    )
    messages.append({"role": "assistant", "content": assistant_prompt})

    # Generate the AI's response
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    reply = response.choices[0].message.content.strip()
    print(f"\nAI: {reply}\n")

    messages.append({"role": "assistant", "content": reply})