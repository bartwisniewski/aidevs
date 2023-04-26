from general.constants import OPENAI_KEY
import requests

URL = "https://api.openai.com/v1/moderations"


def test_results(results):
    return [result.get("flagged") for result in results]


def check(tested_input):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    headers.update({'Authorization': f'Bearer {OPENAI_KEY}'})
    payload = {'input': tested_input}
    try:
        r = requests.post(URL, headers=headers, json=payload)
    except ConnectionError:
        print("problem with connection (wrong server name?)")
        return None
    if r.status_code != 200:
        print(f"Request error: {r.text}")
        return None
    data = r.json()
    results = data.get("results")
    if not results:
        print(f"Wrong answer from Open AI")
        return None
    return test_results(results)
