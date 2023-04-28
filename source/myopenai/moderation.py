from general.constants import OPENAI_KEY
import openai


def test_results(results):
    return [result.get("flagged") for result in results]


def check(tested_input):
    openai.api_key = OPENAI_KEY
    moderation_resp = openai.Moderation.create(input=tested_input)
    results = moderation_resp.get("results")
    if not results:
        print(f"Wrong answer from Open AI")
        return None
    return test_results(results)
