import openai
from os import getenv
from dotenv import load_dotenv

# Загрузите значения из файла .env
load_dotenv()

# Получите значение API-ключа из переменной среды
openai.api_key = getenv("OPENAI_API_KEY")

def ask_chatgpt(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

question = "Какова средняя температура на поверхности Марса?"
answer = ask_chatgpt(question)
print(f"Ответ на вопрос '{question}': {answer}")
