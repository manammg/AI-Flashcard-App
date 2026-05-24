import ollama
import json


def generate_flashcard(topic):
    # دقت کن: بهش گفتیم فقط و فقط JSON بده و هیچ توضیحی نده
    prompt = f"""
    Create a flashcard for: '{topic}'.
    Return ONLY a raw JSON object with keys "question" and "answer".
    Do not include any conversational text or markdown formatting like ```json.
    """

    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])

    content = response['message']['content'].strip()

    # گاهی اوقات AI ممکنه دور جوابش ```json ... ``` بذاره، این رو تمیز می‌کنیم
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


if __name__ == "__main__":
    try:
        card = generate_flashcard("Python List")
        print("Success:", card)
    except Exception as e:
        print("Error details:", e)