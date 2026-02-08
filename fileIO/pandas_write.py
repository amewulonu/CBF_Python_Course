import pandas as pd

dict_example = [
    {"studentId": 1, "name": "Alice", "age": 23},
    {"studentId": 2, "name": "Bob", "age": 25},
    {"studentId": 3, "name": "Charlie", "age": 22},
    {"studentId": 4, "name": "David", "age": 24},
    {"studentId": 5, "name": "Eve", "age": 23},
]


df = pd.DataFrame(dict_example)

print("DataFrame written to 'cbf_write_example.csv'")
print(df)
df.to_csv("cbf_write_example.csv", index=False)