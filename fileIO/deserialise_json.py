import json
with open('course_data.json', 'r') as file:
    data = json.load(file)

print(data,"\n")
print(len(data), "\n")
print(data['students'], "\n")