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
