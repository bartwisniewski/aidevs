
import requests
import json
from requests.exceptions import ConnectionError
from general.constants import SERVER, API_KEY


class Exercise:
    AUTH = "token"
    GET = "task"
    ANSWER = "answer"

    def __init__(self, task_name):
        self.task_name = task_name
        self.token = None
        self.exercise_data = None

    def authorize(self):
        url = f"{SERVER}/{Exercise.AUTH}/{self.task_name}"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        payload = {"apikey": API_KEY}
        try:
            r = requests.post(url, headers=headers, json=payload)
        except ConnectionError:
            print("problem with connection (wrong server name?)")
            return None
        if r.status_code != 200:
            print("problem with authorization wrong API")
            return None
        data = r.json()
        self.token = data.get("token")
        if not self.token:
            print("no token in authorization response")
            return None
        return self.token

    def get_exercise(self):
        if not self.token:
            print("you are not authorized")
            return None
        url = f"{SERVER}/{Exercise.GET}/{self.token}"
        r = requests.get(url)
        if r.status_code != 200:
            print(f"problem with getting exercise: {r.json().get('msg')}")
            return None
        self.exercise_data = r.json()
        if self.exercise_data.get("code") != 0:
            print("wrong return code")
            return None
        return self.exercise_data

    def print_task(self):
        authorised = self.authorize()
        if not authorised:
            return None
        self.get_exercise()
        if self.exercise_data:
            print(f"task: {self.exercise_data.get('msg', 'no task')}")
            pure_data = self.exercise_data.copy()
            pure_data.pop("code")
            pure_data.pop("msg")
            print(f"data: {pure_data}")

    def get_task_data(self):
        authorised = self.authorize()
        if authorised:
            return self.get_exercise()
        return None

    def send_answer(self, answer):
        if not self.token:
            return None
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        url = f"{SERVER}/{Exercise.ANSWER}/{self.token}"
        payload = {"answer": answer}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        return result


def exercise(task_name):
    """Authenticates on AI Devs, gets exercise input data and returns answer as JSON.
    Decorated functions should accept "data": Dict as an argument and should return answer object
    """

    def inner(func):
        def wrapper(*args, **kwargs):
            if not task_name:
                return None
            exercise_obj = Exercise(task_name)
            kwargs["data"] = exercise_obj.get_task_data()
            if not exercise_obj.token:
                return None
            answer = func(*args, **kwargs)
            if answer:
                print(f"answer: {answer}")
                result = exercise_obj.send_answer(answer)
                print(f"result: {result.get('note', 'error')}")

        return wrapper

    return inner
