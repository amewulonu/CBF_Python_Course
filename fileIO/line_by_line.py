#Read up intil the 5th line, the file has 10 lines

# file = open("line_by_line.txt", "r")
# for i, line in enumerate(file):
#     if i == 5: 
#         break
#     print(line.strip())
# file.close() 


#counting the lines of a file

count = 0
file = open("line_by_line.txt", "r")
for line in file:
    # print(line.strip())
    print(line)
    count += 1
file.close()
print("Total number of lines:", count)  


# import csv

# file = open("another_csv.csv", "r", newline='', encoding="utf-8")
# reader = csv.reader(file)
# for row in reader:
#     print(row)
# file.close()


# import json
# file  = open("cbf.json", "r")
# data = json.load(file)
# print(data, "\n")
# for item in data:
#     print(item["name"], item["type"], item["description"])
# file.close()