import json
import os as os
import pandas as pd
import numpy as np

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

df = pd.DataFrame(data)

print(df.head())

#Randomly select 1,000 statements from each verdict type and create a subset:
np.random.seed(0)
sampled_df = df.groupby('verdict').apply(lambda x: x.sample(1000)).reset_index(drop=True)

verdict_counts = sampled_df['verdict'].value_counts().reset_index()
verdict_counts.columns = ['verdict', 'count']
print(verdict_counts)
