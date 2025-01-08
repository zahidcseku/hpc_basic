import pandas as pd
from glob import glob

# set the output directory
output_dir = "fraud_outputs"

# iterate through all the files in output_dir
outputs = []
for file in glob(f"{output_dir}/*.csv"):
    df = pd.read_csv(file, index_col=False)
    outputs.append(df)
    print(df.shape)
    exit()

# merge the results
merged_output = pd.concat(outputs).drop_duplicates().reset_index()

merged_output.to_csv("merged_output.csv", index=False)

print(merged_output.shape)

