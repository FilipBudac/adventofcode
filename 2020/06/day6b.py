with open('input.txt') as file:
    answer_groups = [group.splitlines() for group in file.read().split('\n\n')]

question_groups = [set(''.join(group)) for group in answer_groups]

answered_by_all = 0
for answer_group, question_group in zip(answer_groups, question_groups):
    respondents_count = len(answer_group)
    for question in question_group:
        if ''.join(answer_group).count(question) == respondents_count:
            answered_by_all += 1

print(answered_by_all)
