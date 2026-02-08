import json 
data = {
    "course": "CBF Python Class",
    "students": [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 23}  
    ]
}

#write to json file
with open('course_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

#get a pretty json string
json_text = json.dumps(data, indent=4)
print(json_text)    