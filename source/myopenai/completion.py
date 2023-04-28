from general.constants import OPENAI_KEY
import openai


def format_messages(messages):
    return [{"role": message[0], "content": message[1]} for message in messages]


def chat_completion(model, messages):
    openai.api_key = OPENAI_KEY
    completion = openai.ChatCompletion.create(model=model, messages=messages)
    return completion.choices[0].message.content
