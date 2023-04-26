from general.exercise import exercise
from openai.moderation import check
from openai.completion import send_prompt, single_entry_messages


def classify(info):
    name = info.split()[0]
    return name, info


def organise_data(data):
    organized = {}
    for entry in data:
        key, value = classify(entry)
        organized[key] = value
    return organized


def asked_name(question):
    return question.split()[-1][:-1]


@exercise("inprompt")
def solve(data):
    input_ = data.get("input")
    question = data.get("question")
    organized = organise_data(input_)
    name = asked_name(question)
    info = organized.get(name)
    print(name)
    print(info)
    print(question)
    user_text = f"{info}.{question} Odpowiedz po polsku tylko na to pytanie i nic więcej."
    system_text = "User sends you data about a person and one question. Answer it using only words from question."
    messages = single_entry_messages(user_text=user_text, system_text=system_text)
    response = send_prompt(model="gpt-3.5-turbo", messages=messages)
    choices = response.get("choices")[0]
    message = choices.get("message")
    content = message.get("content")
    print(content)
    answer = content
    return answer


if __name__ == "__main__":
    solve()
