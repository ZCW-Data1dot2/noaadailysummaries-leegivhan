import pandas as pd
import os
import json

def read_json(file_path):
    with open(file_path, "r") as f:
        json_input = json.load(f)
    return json_input

def read_all_json_files(JSON_ROOT):
    df_ex = pd.DataFrame()
    path = JSON_ROOT
    files = os.listdir(path)
    for i in files:
        if ".json" in i:
            j = read_json(path+i)
            df = pd.DataFrame(j['results'])
            df['source'] = i
            df_ex = df_ex.append(df, ignore_index=True)
    return df_ex