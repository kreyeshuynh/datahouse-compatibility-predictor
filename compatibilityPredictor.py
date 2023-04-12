import json

with open('input.json', encoding='utf-8') as f:
    file_contents = json.load(f)

team_attributes = [member['attributes'] for member in file_contents['team']]
applicant_attributes = [member['attributes'] for member in file_contents['applicants']]
team_size = len(team_attributes)

min_values = {}
for attribute in team_attributes[0]:
    min_value = min(member[attribute] for member in team_attributes)
    min_values[attribute] = min_value

min_weight_attributes = []
min_weight_value = min(min_values.values())
for key, value in min_values.items():
    if value == min_weight_value:
        min_weight_attributes.append(key)

compatibility_scores = []
for applicant in file_contents['applicants']:
    score = 0
    for attribute in applicant['attributes']:
        if attribute in min_weight_attributes:
            score += 1 - (applicant['attributes'][attribute] / 100)
        else:
            score += applicant['attributes'][attribute] / 100
    compatibility_scores.append({'name': applicant['name'], 'score': score/len(applicant['attributes'])})

output = {'scoredApplicants': compatibility_scores}

with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)
