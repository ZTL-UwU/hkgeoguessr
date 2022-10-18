def check_ans(usr_end_geo, start_geo, end_geo):
    return abs(usr_end_geo - end_geo) <= abs(end_geo - start_geo) * 1 / 5

K0 = 32

# Correct -> O = 1
# Wrong   -> O = 9
def update_rating(usr, problem, O):
    diff = problem.rating - usr.rating
    P = 1 / (1 + 10 ** (diff / 400))

    problem.answered += 1
    problem.rating -= (K0 + 1 / problem.answered) * abs(diff / 200) * (O - P)
    usr.rating += K0 * (O - P)

    problem.save()
    usr.save()