import numpy as np 
import pandas as pd 


features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 
            'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
            ]
target = "Class"

def get_data(dataloc: str):
    data = pd.read_csv(dataloc, index_col=False)
    print(f"shape of the dataset: {data.shape}")

    traindata = data.sample(frac=.6)
    testdata = data[~data.index.isin(traindata.index)].reset_index(drop=True)
    traindata = traindata.reset_index(drop=True)
    
    print(f"Train data shape: {traindata.shape}")
    print(f"Test data shape: {testdata.shape}")
    
    assert len(traindata) > len(testdata), "Train data should be larger than test data"

    return traindata, testdata



if __name__=="__main__":
    dataloc = "./datasets/creditcard_2023.csv"
    get_data(dataloc=dataloc)