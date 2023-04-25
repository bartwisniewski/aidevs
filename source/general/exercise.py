import os
import requests
import json

from general.constants import SERVER

from dotenv import load_dotenv

load_dotenv()


class Exercise:
    def __init__(self, task_name):
        self.task_name = task_name
        self.token = None
        self.exercise_data = None

    def authorize(self):
        url = f"{SERVER}/token/{self.task_name}"
        payload = {'apikey': os.getenv('API_KEY')}
        r = requests.post(url, data=json.dumps(payload))
        if r.status_code != 200:
            print("problem with authorization")
            return None
        data = r.json()
        self.token = data.get('token')
        return True

    def get_exercise(self):
        if not self.token:
            print("you are not authorized")
            return None
        url = f"{SERVER}/task/{self.token}"
        r = requests.get(url)
        self.exercise_data = r.json()
        return self.exercise_data

    def print_task(self):
        authorised = self.authorize()
        if not authorised:
            return None
        self.get_exercise()
        if self.exercise_data:
            print(f"task: {self.exercise_data.get('msg', 'no task')}")

    def get_task_data(self):
        authorised = self.authorize()
        if authorised:
            return self.get_exercise()
        return None

    def send_answer(self, answer):
        if not self.token:
            return None
        url = f"{SERVER}/answer/{self.token}"
        payload = {'answer': answer}
        r = requests.post(url, data=json.dumps(payload))
        result = r.json()
        return result


def exercise(task_name):
    """ Authenticates on AI Devs, gets exercise input data and returns answer as JSON.
    Decorated functions should accept "data": Dict as an argument and should return answer object"""
    def inner(func):
        def wrapper(*args, **kwargs):
            if not task_name:
                return None
            exercise_obj = Exercise("helloapi")
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


def print_task(task_name):
    """ Authenticates on AI Devs, and prints exercise description"""
    exercise_obj = Exercise(task_name)
    exercise_obj.print_task()
