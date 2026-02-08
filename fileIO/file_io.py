import csv


path = "./students.csv"


with open(path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old and lives in {row['city']}.")
        

# cbf_file = open(path, "r")

# contents = cbf_file.read()
# print(contents)

# cbf_file.close()