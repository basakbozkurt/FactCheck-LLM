import json
import os
import pandas

# Get the path to the user's Documents directory
documents_path = os.path.expanduser('~/Documents/FC_CODE/Kaggle')


file_name = 'politifact_factcheck_data.json'


file_path = os.path.join(documents_path, file_name)


with open(file_path, 'r') as file:
    data = []
    for line in file:
        try:
            json_object = json.loads(line)
            data.append(json_object)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
print(len(data))

df = pandas.DataFrame(data)

print(df.head())




