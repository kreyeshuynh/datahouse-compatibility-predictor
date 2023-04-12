import json

with open('input.json', encoding='utf-8') as f:
    file_contents = json.load(f)

team_attributes = [member['attributes'] for member in file_contents['team']]
team_size = len(team_attributes)

weights = {}

for attribute in team_attributes[0]:
    total_value = sum(member[attribute] for member in team_attributes)
    average_value = total_value / team_size
    weights[attribute] = average_value

print(weights)
