from general.exercise import exercise
from myopenai.completion import chat_completion, format_messages


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
    user_msg = f"{info}.{question} Odpowiedz po polsku tylko na to pytanie i nic więcej."
    system_msg = "User sends you data about a person and one question. Answer it using only words from question."
    messages = format_messages([('user', user_msg), ('system', system_msg)])
    response = chat_completion(model="gpt-3.5-turbo", messages=messages)
    answer = response
    return answer


if __name__ == "__main__":
    solve()
