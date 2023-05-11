from urllib.request import Request, urlopen
from urllib.error import HTTPError

from general.exercise import exercise
from myopenai.completion import chat_completion, format_messages


def urlopen_retry(req, tries):
    counter = 0
    while counter < tries:
        try:
            return urlopen(req).read()
        except HTTPError:
            print("You son of a bitch server")
            counter += 1


def get_text(file_url):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = Request(file_url)
    req.headers.update(hdr)
    b_data = urlopen_retry(req, 3)
    data = b_data.decode('UTF-8')
    return data


@exercise("scraper")
def solve(data):
    file_url = data.get("input")
    question = data.get("question")
    context = get_text(file_url)
    print(context)
    print(question)
    system_msg = """You answer only in polish. 
    You understand english but cannot speak it. 
    Answer only a question given by the user and nothing more"""

    user_msg = f"Based on a given context answer a question in polish and nothing more. " \
               f"context:```{context}```.\nquestion:```{question}```"
    messages = format_messages([("user", user_msg), ("system", system_msg)])
    response = chat_completion(model="gpt-3.5-turbo", messages=messages)
    return response


if __name__ == "__main__":
    solve()
