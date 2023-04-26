from general.exercise import exercise
from openai.moderation import check


@exercise("moderation")
def solve(data):
    input_ = data.get("input")
    answer = check(input_)
    return answer


if __name__ == "__main__":
    solve()
