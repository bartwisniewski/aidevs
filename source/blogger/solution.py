from general.exercise import exercise
from myopenai.completion import chat_completion, format_messages


def titles_to_num_list(topics):
    num_list = ""
    num = 1
    for topic in topics:
        num_list += f"{num}. {topic}. "
        num += 1
    num_list = num_list[:-1]
    return num_list


def clear_answer(answer):
    index = 0
    for p in answer:
        if p == '':
            answer.pop(index)
        else:
            index += 1
    return answer


@exercise("blogger")
def solve(data):
    titles = data.get("blog")
    num_titles = titles_to_num_list(titles)
    print(num_titles)
    system_msg = """You act like a polish culinary blogger. You speak only polish and no other langauge. You are 
    writing blog posts. Write only exactly what user asks you and nothing more. Seperate paragraphs using ###"""

    user_msg = f"Write blog about Pizza Margherita with following {len(titles)} paragraph titles: {num_titles}"
    messages = format_messages([('user', user_msg), ('system', system_msg)])
    response = chat_completion(model="gpt-3.5-turbo", messages=messages)
    response_arr = response.split('###')
    response_arr = clear_answer(response_arr)
    if len(response_arr) != len(titles):
        print(f"Wrong answer from GPT. {response}")
        return None
    return response_arr


@exercise("blogger")
def solve_iter(data):
    response = []
    titles = data.get("blog")
    print(titles)
    system_msg = "You act like a polish culinary blogger. You speak only polish and no other langauge. You are " \
                 "writing blog post about Pizza Margherita Write only exactly what user asks you and nothing more."
    for title in titles:
        user_msg = f"Write blog paragraph with title: {title}"
        messages = format_messages([('user', user_msg), ('system', system_msg)])
        response.append(chat_completion(model="gpt-3.5-turbo", messages=messages))
    return response


if __name__ == "__main__":
    solve()
