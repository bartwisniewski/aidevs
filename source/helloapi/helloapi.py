from general.exercise import print_task
from general.exercise import exercise


@exercise("helloapi")
def solve(data):
    answer = data.get("cookie")
    return answer


if __name__ == "__main__":
    print_task("helloapi")
    solve()

