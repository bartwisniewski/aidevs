from general.constants import OPENAI_KEY
import requests

URL = "https://api.openai.com/v1/chat/completions"


def single_entry_messages(user_text: str, system_text: str):
    messages = [{"role": "user", "content": user_text},
                {"role": "system", "content": system_text}]
    return messages


def send_prompt(model, messages):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    headers.update({'Authorization': f'Bearer {OPENAI_KEY}'})
    payload = {'model': model, 'messages': messages}
    try:
        r = requests.post(URL, headers=headers, json=payload)
    except ConnectionError:
        print("problem with connection (wrong server name?)")
        return None
    if r.status_code != 200:
        print(f"Request error: {r.text}")
        return None
    response = r.json()
    return response
