import re


"""
Update problem & user ELO

Correct -> O = 1
Wrong   -> O = 9
"""
K0 = 32
def update_rating(usr, problem, O):
    diff = problem.rating - usr.rating
    P = 1 / (1 + 10 ** (diff / 400))

    usr.answered += 1
    problem.answered += 1
    if O == 1:
        problem.correct += 1
    else:
        problem.wrong += 1

    problem.rating -= (K0 + 1 / problem.answered) * abs(diff / 200) * (O - P)
    usr.rating += K0 * (O - P)

    problem.save()
    usr.save()


# Check user answer
def check_ans_money(usr_end_geo, start_geo, end_geo):
    return abs(usr_end_geo - end_geo) <= abs(end_geo - start_geo) * 1 / 5

def check_ans_place(user_place, ans_place):
    return user_place == ans_place


# Check registration email
def is_email(str):
    p = re.compile(r"^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$")

    if p.match(str):
        return True
    else:
        return False
