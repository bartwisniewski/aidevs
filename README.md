# aidevs
AI Devs course - exercises

this is a place where I store my exercises for AI Devs course. The course is about learning programming with use of latest AI technology as an assistance. Is will mainly use power of GPT4 model connected to some no-code / automatization tools to write applications and integrations faster.

# How to run:

- Get repository
```
git pull https://github.com/bartwisniewski/aidevs
```

- Create Virtual Environment
```

cd ai-devs
python3 -m venv ./env
```

- Activate Virtual Environment
```
source env/bin/activate (Windows: env\Scripts\activate.bat)
```

- Install dependencies
```
pip install -r requirements.txt
```

- Prepare your environment variables (API KEYS)
```
cp source/general/.env_example source/general/.env (Windows: copy source\general\.env_example source\general\.env)
```
open /source/general/.env and input your private API KEYs

# New exercise
- Create new directory in sources. Directory name should be the same as exercise name
- Copy task.py from any existing exercise packages
- Run task.py. It should display the task description
- Create new python file
- Import exercise decorator 
- Import chat_completion from myopenai
- Write a function with data as a first parameter (this is what you get from aidevs)
- Decorate a function with exercise decorator and exercise name as an argument
- Return answer
- Call your function without parameter inside the file and run it

Example:

```
from general.exercise import exercise
from myopenai.completion import chat_completion, format_messages


@exercise("inprompt")
def solve(data):
    # do something with data to prepare messages for GPT
    messages = format_messages[('user','message1'), ('system', 'message2')]
    answer = chat_completion(model="gpt-3.5-turbo", messages=messages)
    return answer


if __name__ == "__main__":
    solve()
```

